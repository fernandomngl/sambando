import wx
from smb.SMBConnection import SMBConnection
import os
from os import path
import configparser
import re
import filecmp
import zipfile
import psutil
from forms import Sambando, Config

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
        
        self.txLogin.SetValue(login)
        self.txPassword.SetValue(password)
        self.txDomain.SetValue(domain)
        self.txPath.SetValue(path)
        self.txCompareFile.SetValue(comparefile)

