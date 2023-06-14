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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AI Audio Generator", pos = wx.DefaultPosition, size = wx.Size( 800,675 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer5 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableRow( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer6 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer6.AddGrowableCol( 1 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblPrompt = wx.StaticText( self, wx.ID_ANY, u"Prompt::", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPrompt.Wrap( -1 )

		fgSizer6.Add( self.lblPrompt, 0, wx.ALL, 5 )

		self.txtPrompt = wx.TextCtrl( self, wx.ID_ANY, u"80s electronic track with melodic synthesizers, catchy beat and groovy bass", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer6.Add( self.txtPrompt, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer7 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer7.AddGrowableCol( 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblDuration = wx.StaticText( self, wx.ID_ANY, u"Duration:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDuration.Wrap( -1 )

		fgSizer7.Add( self.lblDuration, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.spnDuration = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 30, 15 )
		fgSizer7.Add( self.spnDuration, 0, wx.ALL|wx.EXPAND, 5 )

		self.lblGenerations = wx.StaticText( self, wx.ID_ANY, u"Generaations:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblGenerations.Wrap( -1 )

		fgSizer7.Add( self.lblGenerations, 0, wx.ALL, 5 )

		self.spnGenerations = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 5, 5 )
		fgSizer7.Add( self.spnGenerations, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.lblOverlap = wx.StaticText( self, wx.ID_ANY, u"Overlap:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblOverlap.Wrap( -1 )

		fgSizer7.Add( self.lblOverlap, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.spnOverlap = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 29, 5 )
		fgSizer7.Add( self.spnOverlap, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( fgSizer7, 1, wx.EXPAND, 5 )

		self.btnGenerate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnGenerate, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblModel = wx.StaticText( self, wx.ID_ANY, u"Model:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblModel.Wrap( -1 )

		bSizer4.Add( self.lblModel, 0, wx.ALL, 5 )

		chcModelChoices = [ u"small", u"medium", u"large" ]
		self.chcModel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chcModelChoices, 0 )
		self.chcModel.SetSelection( 0 )
		bSizer4.Add( self.chcModel, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		fgSizer6.Add( bSizer3, 1, wx.EXPAND, 5 )


		fgSizer5.Add( fgSizer6, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 7, 3, 0, 0 )
		fgSizer8.AddGrowableCol( 1 )
		fgSizer8.AddGrowableRow( 1 )
		fgSizer8.AddGrowableRow( 2 )
		fgSizer8.AddGrowableRow( 3 )
		fgSizer8.AddGrowableRow( 4 )
		fgSizer8.AddGrowableRow( 5 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblMain = wx.StaticText( self, wx.ID_ANY, u"Main:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMain.Wrap( -1 )

		fgSizer8.Add( self.lblMain, 0, wx.ALL, 5 )

		self.mctrlMain = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlMain.SetPlaybackRate(1)
		self.mctrlMain.SetVolume(1)
		fgSizer8.Add( self.mctrlMain, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )

		self.btnLoad = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnLoad, 0, wx.ALL, 5 )

		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnSave, 0, wx.ALL, 5 )

		self.btnClear = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnClear, 0, wx.ALL, 5 )


		fgSizer8.Add( gSizer2, 1, wx.EXPAND, 5 )

		self.lblOption1 = wx.StaticText( self, wx.ID_ANY, u"Option 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblOption1.Wrap( -1 )

		fgSizer8.Add( self.lblOption1, 0, wx.ALL, 5 )

		self.mctrlOption1 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption1.SetPlaybackRate(1)
		self.mctrlOption1.SetVolume(1)
		fgSizer8.Add( self.mctrlOption1, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnOption1 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btnOption1, 0, wx.ALL, 5 )

		self.lblOption2 = wx.StaticText( self, wx.ID_ANY, u"Option 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblOption2.Wrap( -1 )

		fgSizer8.Add( self.lblOption2, 0, wx.ALL, 5 )

		self.mctrlOption2 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption2.SetPlaybackRate(1)
		self.mctrlOption2.SetVolume(1)
		fgSizer8.Add( self.mctrlOption2, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnOption2 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btnOption2, 0, wx.ALL, 5 )

		self.lblOption3 = wx.StaticText( self, wx.ID_ANY, u"Option 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblOption3.Wrap( -1 )

		fgSizer8.Add( self.lblOption3, 0, wx.ALL, 5 )

		self.mctrlOption3 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption3.SetPlaybackRate(1)
		self.mctrlOption3.SetVolume(1)
		fgSizer8.Add( self.mctrlOption3, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnOption3 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btnOption3, 0, wx.ALL, 5 )

		self.lblOption4 = wx.StaticText( self, wx.ID_ANY, u"Option 4:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblOption4.Wrap( -1 )

		fgSizer8.Add( self.lblOption4, 0, wx.ALL, 5 )

		self.mctrlOption4 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption4.SetPlaybackRate(1)
		self.mctrlOption4.SetVolume(1)
		fgSizer8.Add( self.mctrlOption4, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnOption4 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btnOption4, 0, wx.ALL, 5 )

		self.lblOption5 = wx.StaticText( self, wx.ID_ANY, u"Option 5:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblOption5.Wrap( -1 )

		fgSizer8.Add( self.lblOption5, 0, wx.ALL, 5 )

		self.mctrlOption5 = wx.media.MediaCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		self.mctrlOption5.SetPlaybackRate(1)
		self.mctrlOption5.SetVolume(1)
		fgSizer8.Add( self.mctrlOption5, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnOption5 = wx.Button( self, wx.ID_ANY, u"Keep", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.btnOption5, 0, wx.ALL, 5 )

		self.lblStatusLabel = wx.StaticText( self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblStatusLabel.Wrap( -1 )

		fgSizer8.Add( self.lblStatusLabel, 0, wx.ALL, 5 )

		self.lblStatus = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblStatus.Wrap( -1 )

		fgSizer8.Add( self.lblStatus, 0, wx.ALL|wx.EXPAND, 5 )

		self.progress_bar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.progress_bar.SetValue( 0 )
		fgSizer8.Add( self.progress_bar, 0, wx.ALL, 5 )


		fgSizer5.Add( fgSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


