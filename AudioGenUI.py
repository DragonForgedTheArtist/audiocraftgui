# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.media

###########################################################################
## Class AudioGenUI
###########################################################################

class AudioGenUI ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AudioGen", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblPrompt = wx.StaticText( self, wx.ID_ANY, u"Prompt:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPrompt.Wrap( -1 )

		fgSizer2.Add( self.lblPrompt, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txtPrompt = wx.TextCtrl( self, wx.ID_ANY, u"80s pop track with bassy drums and synth", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer2.Add( self.txtPrompt, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Duration:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.spnDuration = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 30, 15 )
		fgSizer3.Add( self.spnDuration, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Generations:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.spnGenerations = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 5, 5 )
		fgSizer3.Add( self.spnGenerations, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Overlap:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.spnOverlap = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 2, 30, 5 )
		fgSizer3.Add( self.spnOverlap, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer3, 0, wx.EXPAND, 5 )

		self.btnGenerate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnGenerate, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Model:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer2.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		chcModelChoices = [ u"small", u"medium", u"large" ]
		self.chcModel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chcModelChoices, 0 )
		self.chcModel.SetSelection( 0 )
		bSizer2.Add( self.chcModel, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( bSizer2, 1, wx.EXPAND, 5 )


		fgSizer2.Add( bSizer2, 0, 0, 5 )


		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 7, 3, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableRow( 1 )
		fgSizer4.AddGrowableRow( 2 )
		fgSizer4.AddGrowableRow( 3 )
		fgSizer4.AddGrowableRow( 4 )
		fgSizer4.AddGrowableRow( 5 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Main Track", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.mctrlMain = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlMain.SetPlaybackRate(1)
		self.mctrlMain.SetVolume(1)
		fgSizer4.Add( self.mctrlMain, 0, wx.ALL|wx.EXPAND, 2 )

		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )

		self.btnLoad = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnLoad, 0, wx.ALL, 5 )

		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnSave, 0, wx.ALL, 5 )

		self.btnClear = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnClear, 0, wx.ALL, 5 )


		fgSizer4.Add( gSizer1, 1, 0, 0 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Option 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.mctrlOption1 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption1.SetPlaybackRate(1)
		self.mctrlOption1.SetVolume(1)
		fgSizer4.Add( self.mctrlOption1, 1, wx.ALL|wx.EXPAND, 2 )

		self.btnOption1 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnOption1, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Option 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.mctrlOption2 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption2.SetPlaybackRate(1)
		self.mctrlOption2.SetVolume(1)
		fgSizer4.Add( self.mctrlOption2, 0, wx.ALL|wx.EXPAND, 2 )

		self.btnOption2 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnOption2, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Option 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		fgSizer4.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.mctrlOption3 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption3.SetPlaybackRate(1)
		self.mctrlOption3.SetVolume(1)
		fgSizer4.Add( self.mctrlOption3, 0, wx.ALL|wx.EXPAND, 2 )

		self.btnOption3 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnOption3, 0, wx.ALL, 5 )

		self.m_staticText611 = wx.StaticText( self, wx.ID_ANY, u"Option 4:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611.Wrap( -1 )

		fgSizer4.Add( self.m_staticText611, 0, wx.ALL, 5 )

		self.mctrlOption4 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption4.SetPlaybackRate(1)
		self.mctrlOption4.SetVolume(1)
		fgSizer4.Add( self.mctrlOption4, 0, wx.ALL|wx.EXPAND, 2 )

		self.btnOption4 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnOption4, 0, wx.ALL, 5 )

		self.m_staticText6111 = wx.StaticText( self, wx.ID_ANY, u"Option 5:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6111.Wrap( -1 )

		fgSizer4.Add( self.m_staticText6111, 0, wx.ALL, 5 )

		self.mctrlOption5 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption5.SetPlaybackRate(1)
		self.mctrlOption5.SetVolume(1)
		fgSizer4.Add( self.mctrlOption5, 0, wx.ALL|wx.EXPAND, 2 )

		self.btnOption5 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnOption5, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.lblStatus = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblStatus.Wrap( -1 )

		fgSizer4.Add( self.lblStatus, 0, wx.ALL|wx.EXPAND, 5 )

		self.progress_bar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.BORDER_SUNKEN )
		self.progress_bar.SetValue( 0 )
		fgSizer4.Add( self.progress_bar, 0, wx.ALL, 5 )


		fgSizer1.Add( fgSizer4, 1, wx.EXPAND, 0 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


