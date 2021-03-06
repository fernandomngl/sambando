import wx
from smb.SMBConnection import SMBConnection
import os
from os import path
import configparser
import re
import filecmp
import zipfile
import psutil
from forms import Sambando, Config, Licenses

class Configure(Config.frConfig):
    
    def onCancel(self, event):
        self.Close()
    
    def onSave(self, event):
        config = configparser.ConfigParser()
        configpath = 'sambando.ini'
        
        config['NETWORK'] = {
            'login' : self.txLogin.GetValue(),
            'password' : self.txPassword.GetValue(),
            'domain' : self.txDomain.GetValue(),
            'path' : self.txPath.GetValue(),
        }
        
        config['DO'] = {
            'automatic' : str(self.chkAutomatic.IsChecked()),
            'directory' : str(self.chkDirectory.IsChecked()),
            'compare' : str(self.chkCompareFile.IsChecked()),
            'lock' : str(self.chkLock.IsChecked()),
            'extract' : str(self.chkExtract.IsChecked()),
            'file' : self.txCompareFile.GetValue(),
            'program1' : '', #software to run after will be checked from this entries
            'program2' : '',
            'program3' : '',
            'program4' : '',
        }
        
        with open(configpath, 'w') as configfile:
            config.write(configfile)
        
        self.Close()

    def fillForm(self, event):
        config = configparser.ConfigParser()
        configpath = 'sambando.ini'
        
        if not config.read(configpath):
            config['NETWORK'] = {
               'login' : 'guest',
               'password' : 'guest',
               'domain' : 'workspace',
               'path' :  os.sep+os.sep+'server'+os.sep+'share'+os.sep+'folder',
            }
         
            config['DO'] = {
                'automatic' : str(self.chkAutomatic.IsChecked()),
                'directory' : str(self.chkDirectory.IsChecked()),
                'compare' : str(self.chkCompareFile.IsChecked()),
                'extract' : str(self.chkExtract.IsChecked()),
                'lock' : str(self.chkLock.IsChecked()),
                'file' : self.txCompareFile.GetValue(),
                'program1' : '', #software to run after will be checked from this entries
                'program2' : '',
                'program3' : '',
                'program4' : '',
            }
            
            with open(configpath, 'w') as configfile:
                config.write(configfile)
        
        login = config['NETWORK']['login']
        password = config['NETWORK']['password']
        domain = config['NETWORK']['domain']
        path = config['NETWORK']['path']
        comparefile = config['DO']['file']
        
        self.chkAutomatic.SetValue(config.getboolean('DO', 'automatic'))
        self.chkDirectory.SetValue(config.getboolean('DO', 'directory'))
        self.chkCompareFile.SetValue(config.getboolean('DO','compare'))
        self.chkLock.SetValue(config.getboolean('DO','lock'))
        self.chkExtract.SetValue(config.getboolean('DO','extract'))
        
        self.txLogin.SetValue(login)
        self.txPassword.SetValue(password)
        self.txDomain.SetValue(domain)
        self.txPath.SetValue(path)
        self.txCompareFile.SetValue(comparefile)

class Update(Sambando.frSambando):
    def onConfig(self, event):
        configure = Configure(self)
        configure.Show()

    def onShow(self, event):
        self.ggUpdate.Hide()

    def onUpdate(self, event):
        config = configparser.ConfigParser()
        configpath = 'sambando.ini'
        config.read(configpath)
        
        login = config['NETWORK']['login']
        password = config['NETWORK']['password']
        domain = config['NETWORK']['domain']
        path = config['NETWORK']['path']
        is_dir = config.getboolean('DO', 'directory')
        is_compared = config.getboolean('DO', 'compare')
        is_extracted = config.getboolean('DO', 'extract')
        is_locked = config.getboolean('DO', 'lock')
        compare_file = ''
        if is_compared:
            compare_file = config['DO']['file']
        
        rgx_sysinpath = re.compile(r'%s%s((\w)|(\d)|[.])+%s' % (
            os.sep if os.sep != '\\' else '\\\\', #because in Windows the path is the same character that escapes special chars
            os.sep if os.sep != '\\' else '\\\\',
            os.sep if os.sep != '\\' else '\\\\', )
        )
        
        system_name = rgx_sysinpath.search(path.lstrip('smb:'))[0].replace(os.sep,'')
        share_start_index = len(system_name)+3 #without the first \\ and the \ from the system_name
        share_end_index = path.find(os.sep, share_start_index, len(path)) #until the first \ or / after the system_name

        if share_end_index == -1:
            share_end_index = len(path) #the share is the folder or it have an unterminated folder as param
        
        
        share = path[share_start_index:share_end_index]
        folder = path[share_end_index:]
        
        dirfile = ''
        if is_dir:
            folder = folder.rstrip(os.sep)+os.sep #if it is dir ends with folder separator
        else:
            folder = folder.rstrip(os.sep)
            index_sep = folder.rfind(os.sep)
            if index_sep == -1:
                dirfile = '%s' % folder
                folder = ''+os.sep
            else:
                dirfile = folder[index_sep+1:]
                folder = folder.rstrip(dirfile)+os.sep
                
            
        conn = SMBConnection(login,password,'enumerator',system_name,domain,use_ntlm_v2=True,
                                 sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
            is_direct_tcp=True)
        connected = conn.connect(system_name,445)
       
        if is_compared: 
            file_comparison = open(compare_file+'_new', 'wb')
            conn.retrieveFileFromOffset(share, 'versao', file_comparison, 0, -1)
            file_comparison.close()        
        
        
        def smbtree(smbconn, shareddevice, top, download):
            filecount = 0
            names = smbconn.listPath(shareddevice, top)
            #print(str(names))
            for name in names:
                if name.isDirectory:
                    if name.filename not in [u'.', u'..']:
                        new_shareddevice = os.path.join(top.lstrip(os.sep),name.filename)+os.sep
                        new_conn = SMBConnection(login,password,'enumerator',system_name,domain,use_ntlm_v2=True,
                                                         sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
                                    is_direct_tcp=True)
                        new_conn.connect(system_name,445)
                        try:
                            if is_dir:
                                os.makedirs(new_shareddevice.lstrip(folder[1:]))    
                        except FileExistsError:
                            pass
                        #print(new_shareddevice)
                        filecount+=smbtree(new_conn,shareddevice, new_shareddevice, download)
                        new_conn.close()
                else:
                    filecount+=1
                    if download and name.filename != dirfile and is_dir:
                        self.lbUpdate.Append(top.lstrip(os.sep)+name.filename)
                        self.lbUpdate.SetSelection(self.lbUpdate.GetCount()-1)
                        self.ggUpdate.SetValue(self.ggUpdate.GetValue()+1)
                        relfilepath = top.lstrip(folder)+name.filename
                        #print(top+name.filename)
                        newfile = open(relfilepath, "wb")
                        smbconn.retrieveFileFromOffset(shareddevice, top+name.filename, newfile, 0, -1)
                        newfile.close()
                        wx.Yield()
                    elif not is_dir and download and name.filename == dirfile:
                        self.lbUpdate.Append('Downloading '+top.lstrip(os.sep)+name.filename)
                        self.lbUpdate.SetSelection(self.lbUpdate.GetCount()-1)
                        self.ggUpdate.SetValue(self.ggUpdate.GetValue()+1)
                        wx.Yield()
                        relfilepath = name.filename
                        topname = top.rstrip(os.sep)+os.sep+name.filename.lstrip(os.sep)
                        #print('topname '+topname)
                        newfile = open(relfilepath, "wb")
                        smbconn.retrieveFileFromOffset(shareddevice, topname, newfile, 0, -1)
                        newfile.close()
                        if dirfile.endswith('.zip') and is_extracted:
                            self.lbUpdate.Append('Extracting...')
                            self.ggUpdate.SetValue(self.ggUpdate.GetValue())
                            wx.Yield()
                            try:
                                zip_ref = zipfile.ZipFile(share+'.zip', 'r')
                                self.ggUpdate.Show()
                                for filename in zip_ref.namelist():
                                    zip_ref.extract(filename)
                                    next_value = self.ggUpdate.GetValue()+1
                                    self.ggUpdate.SetValue(next_value)
                                    self.lbUpdate.Append(filename)
                                    self.lbUpdate.SetSelection(next_value)
                                    wx.Yield()
                            except:
                                self.lbUpdate.Append('ERROR!')
                            finally:
                                zip_ref.close()
        
            return filecount

        program_list = {
            config['DO']['program1'] if config.has_option('DO','program1') else '',
            config['DO']['program2'] if config.has_option('DO','program2') else '',
            config['DO']['program3'] if config.has_option('DO','program3') else '',
            config['DO']['program4'] if config.has_option('DO','program4') else '',        
        } 

    
        if( not os.path.isfile(compare_file) or not filecmp.cmp(compare_file+'_new',compare_file)):
            program_open = True
            while is_locked and program_open:
                program_open = False
                for p in psutil.process_iter():
                    procinfo = p.as_dict(attrs=['name','pid','username'])
                    for program in program_list:
                        if program ==  '':
                            continue
                        if program in procinfo['name'].lower():
                            dlg = wx.MessageBox('Please close '+procinfo['name']+' to update!', 'Process open',wx.OK|wx.CANCEL|wx.ICON_EXCLAMATION)
                            if dlg == wx.CANCEL :
                                return
                            program_open = True
            totalcount = smbtree(conn,share,folder, False)
            #print('totalcount'+str(totalcount))
            self.ggUpdate.SetRange(totalcount)
            self.ggUpdate.Show()
            wx.Yield()
    
            smbtree(conn,share,folder, True)
    
            self.ggUpdate.Hide()
            self.stUpdateResult.SetLabel('Updated successfully!')
            wx.Yield()
            #print(str(self.ggUpdate.GetValue()))
    
            wx.Sleep(3)
        else:
            self.stUpdateResult.SetLabel('No new files!')
            self.Update()
            wx.MilliSleep(800)
    
        conn.close()
    
        try:
            if config.has_option('APP', 'program1'):
                os.startfile(config['APP']['program1'])
            if config.has_option('APP', 'program2'):
                os.startfile(config['APP']['program2'])
            if config.has_option('APP', 'program3'):
                os.startfile(config['APP']['program3'])
            if config.has_option('APP', 'program4'):
                os.startfile(config['APP']['program4'])
        except:
            pass
    
        self.Close()

    def onLicenses(self, event):
        license = Licenses(self)
        license.Show()
        
class Licenses(Licenses.frLicenses):
    pass
        

app = wx.App()
mainWindow = Update(None)
mainWindow.Show()
if not path.exists('sambando.ini'):
    mainWindow.onConfig(mainWindow)
else:
    config = configparser.ConfigParser()
    configpath = 'sambando.ini'

    config.read(configpath)
    try:
        if config.getboolean('DO','automatic'):
            wx.Yield()
            mainWindow.onUpdate(mainWindow)
    except:
        pass        
app.MainLoop()