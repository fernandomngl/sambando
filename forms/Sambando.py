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
## Class frSambando
###########################################################################

class frSambando ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 277,469 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_SHAPED|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetExtraStyle( wx.WS_EX_PROCESS_UI_UPDATES )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        szSambando = wx.BoxSizer( wx.VERTICAL )

        szSambando.SetMinSize( wx.Size( 320,200 ) )
        self.pnSambando = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.pnSambando.SetExtraStyle( wx.WS_EX_PROCESS_UI_UPDATES )

        szPn = wx.BoxSizer( wx.VERTICAL )

        self.stTitle = wx.StaticText( self.pnSambando, wx.ID_ANY, u"Updater", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stTitle.Wrap( -1 )

        szPn.Add( self.stTitle, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        lbUpdateChoices = []
        self.lbUpdate = wx.ListBox( self.pnSambando, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbUpdateChoices, wx.LB_HSCROLL )
        self.lbUpdate.SetExtraStyle( wx.WS_EX_PROCESS_UI_UPDATES )
        self.lbUpdate.SetMinSize( wx.Size( 240,280 ) )

        szPn.Add( self.lbUpdate, 0, wx.ALIGN_CENTER_HORIZONTAL, 10 )

        self.ggUpdate = wx.Gauge( self.pnSambando, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.ggUpdate.SetValue( 0 )
        self.ggUpdate.Enable( False )
        self.ggUpdate.SetMinSize( wx.Size( 400,20 ) )

        szPn.Add( self.ggUpdate, 0, wx.ALL|wx.BOTTOM, 10 )


        szPn.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btnUpdate = wx.Button( self.pnSambando, wx.ID_ANY, u"Update!", wx.DefaultPosition, wx.DefaultSize, 0 )
        szPn.Add( self.btnUpdate, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

        self.stUpdateResult = wx.StaticText( self.pnSambando, wx.ID_ANY, u"https://github.com/fernandomngl/sambando", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stUpdateResult.Wrap( -1 )

        szPn.Add( self.stUpdateResult, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.pnSambando.SetSizer( szPn )
        self.pnSambando.Layout()
        szPn.Fit( self.pnSambando )
        szSambando.Add( self.pnSambando, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( szSambando )
        self.Layout()
        self.mbSambando = wx.MenuBar( 0 )
        self.mnUpdate = wx.Menu()
        self.itmConfig = wx.MenuItem( self.mnUpdate, wx.ID_ANY, u"Config", wx.EmptyString, wx.ITEM_NORMAL )
        self.mnUpdate.Append( self.itmConfig )

        self.mbSambando.Append( self.mnUpdate, u"File" )

        self.SetMenuBar( self.mbSambando )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.onShow )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.onUpdate )
        self.Bind( wx.EVT_MENU, self.onConfig, id = self.itmConfig.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onShow( self, event ):
        event.Skip()

    def onUpdate( self, event ):
        event.Skip()

    def onConfig( self, event ):
        event.Skip()