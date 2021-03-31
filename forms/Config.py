# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frConfig
###########################################################################

class frConfig ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 477,318 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.FRAME_SHAPED|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        szConfig = wx.BoxSizer( wx.VERTICAL )

        self.pnConfig = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        szPn = wx.FlexGridSizer( 0, 2, 0, 0 )
        szPn.SetFlexibleDirection( wx.BOTH )
        szPn.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.stTitle = wx.StaticText( self.pnConfig, wx.ID_ANY, u"Network credentials", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stTitle.Wrap( -1 )

        szPn.Add( self.stTitle, 0, wx.ALL, 5 )


        szPn.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.stLogin = wx.StaticText( self.pnConfig, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stLogin.Wrap( -1 )

        szPn.Add( self.stLogin, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.txLogin = wx.TextCtrl( self.pnConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txLogin.SetMinSize( wx.Size( 300,-1 ) )

        szPn.Add( self.txLogin, 0, wx.ALL, 5 )

        self.stPassword = wx.StaticText( self.pnConfig, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stPassword.Wrap( -1 )

        szPn.Add( self.stPassword, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.txPassword = wx.TextCtrl( self.pnConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        self.txPassword.SetMinSize( wx.Size( 300,-1 ) )

        szPn.Add( self.txPassword, 0, wx.ALL, 5 )

        self.stDomain = wx.StaticText( self.pnConfig, wx.ID_ANY, u"Domain", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stDomain.Wrap( -1 )

        szPn.Add( self.stDomain, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.txDomain = wx.TextCtrl( self.pnConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txDomain.SetMinSize( wx.Size( 300,-1 ) )

        szPn.Add( self.txDomain, 0, wx.ALL, 5 )

        self.stPath = wx.StaticText( self.pnConfig, wx.ID_ANY, u"Path", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stPath.Wrap( -1 )

        szPn.Add( self.stPath, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.txPath = wx.TextCtrl( self.pnConfig, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txPath.SetMinSize( wx.Size( 300,-1 ) )

        szPn.Add( self.txPath, 0, wx.ALL, 5 )

        self.chkAutomatic = wx.CheckBox( self.pnConfig, wx.ID_ANY, u"Automatic", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkAutomatic.SetValue(True)
        szPn.Add( self.chkAutomatic, 0, wx.ALL, 5 )

        self.chkDirectory = wx.CheckBox( self.pnConfig, wx.ID_ANY, u"Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkDirectory.SetValue(True)
        szPn.Add( self.chkDirectory, 0, wx.ALL, 5 )

        self.btnSave = wx.ToggleButton( self.pnConfig, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        szPn.Add( self.btnSave, 0, wx.ALL|wx.BOTTOM, 5 )

        self.btnCancel = wx.ToggleButton( self.pnConfig, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        szPn.Add( self.btnCancel, 0, wx.ALL|wx.BOTTOM, 5 )


        self.pnConfig.SetSizer( szPn )
        self.pnConfig.Layout()
        szPn.Fit( self.pnConfig )
        szConfig.Add( self.pnConfig, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( szConfig )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.fillForm )
        self.btnSave.Bind( wx.EVT_TOGGLEBUTTON, self.onSave )
        self.btnCancel.Bind( wx.EVT_TOGGLEBUTTON, self.onCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def fillForm( self, event ):
        event.Skip()

    def onSave( self, event ):
        event.Skip()

    def onCancel( self, event ):
        event.Skip()