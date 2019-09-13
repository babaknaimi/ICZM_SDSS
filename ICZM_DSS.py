# -*- coding: utf-8 -*-

import sys, time
import os
import sip
import shutil
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from frmIdentify import *
import osgeo.ogr as ogr
from frmMap import *
from funcZoneDialog import *
from formEcologicDialog import *
from formHazardDialog import *
from formOptThreatDialog import *
from frmHelpView import *
from frmPassword import *
from collections import OrderedDict
from arcgisDialog import *
from PyQt4 import QtWebKit
from PyQt4 import QtNetwork
from random import randint


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)



class TOCListWidget(QListWidget):
    itemMoved = pyqtSignal(int, int, QListWidgetItem)
    def __init__(self,parent=None, **args):
        super(TOCListWidget,self).__init__(parent, **args)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.drag_item = None
        self.drag_row = None

    def dropEvent(self, event):
         super(TOCListWidget, self).dropEvent(event)
         self.itemMoved.emit(self.drag_row, self.row(self.drag_item),self.drag_item)
         self.drag_item = None

    def startDrag(self, supportedActions):
         self.drag_item = self.currentItem()
         self.drag_row = self.row(self.drag_item)
         super(TOCListWidget, self).startDrag(supportedActions)



class TOCListModel(QAbstractListModel):
    Mimetype = 'application/vnd.row.list'
    def __init__(self,data=[],parent=None):
        QAbstractListModel.__init__(self,parent)
        self.__data=data

    def rowCount(self,parent):
        return len(self.__data)

    def flags(self, index):
        flags = super(TOCListModel, self).flags(index)
        if index.isValid():
            flags |= Qt.ItemIsEditable
            flags |= Qt.ItemIsDragEnabled
        else:
            flags = Qt.ItemIsDropEnabled

        return flags

    def insertRows(self, row, count, parent=QModelIndex()):

        self.beginInsertRows(QModelIndex(), row, row + count - 1)
        self.__data[row:row] = [''] * count
        self.endInsertRows()
        return True

    def mimeData(self, indexes):
        sortedIndexes = sorted([index for index in indexes
            if index.isValid()], key=lambda index: index.row())
        encodedData = '\n'.join(self.data(index, Qt.DisplayRole)
                for index in sortedIndexes)
        mimeData = QMimeData()
        mimeData.setData(self.Mimetype, encodedData)
        return mimeData

    def mimeTypes(self):
        return [self.Mimetype]

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        del self.__data[row:row + count]
        self.endRemoveRows()
        return True

    def data(self,index,role):
        if not index.isValid():
            return None
        if index.row() > len(self.__data):
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.__data[index.row()]

        return None

    def dropMimeData(self, data, action, row, column, parent):
        if action == Qt.IgnoreAction:
            return True
        if not data.hasFormat(self.Mimetype):
            return False
        if column > 0:
            return False

        strings = str(data.data(self.Mimetype)).split('\n')
        self.insertRows(row, len(strings))
        for i, text in enumerate(strings):
            self.setData(self.index(row + i, 0), text)

        return True

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False

        self.__data[index.row()] = value
        self.dataChanged.emit(index, index)
        return True

    def supportedDropActions(self):
        return Qt.MoveAction



class iczmDSS(QMainWindow):
    def __init__(self,parent=None):
        super(iczmDSS,self).__init__(parent)

        self.x=None
        self.y=None
        self.Extracted=False
        self.selectedProvince=''
        self.where=None



        self.fZone=False
        self.fRisk=False
        self.fOpt=False
        self.fEcol=False
        self.fHlp=False
        self.reportName=""

        self.North_Files=['Zoning_North','ManageB_North','Hazards_North','Opportunity_North','Threat_North','Tavan_North']
        self.South_Files=['Zoning_South','ManageB_South','Hazards_South','Opportunity_South','Threat_South','Tavan_South']
        self.South_SpecialFiles=['Zoning_South','ManageB_South']
        self.North_SpecialFiles=["Zoning_North",'ManageB_North']
        self.FieldNames={}
        self.FieldNames['Zoning_North']=['Result','Name','Regulation','Code']
        self.FieldNames['ManageB_North']=['name','MC','Code']
        self.FieldNames['Hazards_North']=['R','Q','L','F','I','K','S']
        self.FieldNames['Opportunity_North']=['O_Agri','O_Indust','O_Resid','O_Tour']
        self.FieldNames['Threat_North']=['T_Agri','T_Indust','T_Resid','T_Tour']
        self.FieldNames['Tavan_North']=['P_Agri','P_Urban','P_Indust','P_Tour','P_Conserv']

        self.FieldNames['Zoning_South']=['Result','Name','Regulation','Code']
        self.FieldNames['ManageB_South']=['Name','MC','Code']
        self.FieldNames['Hazards_South']=['R','Q','L','K','S']
        self.FieldNames['Opportunity_South']=['O_Agri','O_Indust','O_Resid','O_Tour']
        self.FieldNames['Threat_South']=['T_Agri','T_Indust','T_Resid','T_Tour']
        self.FieldNames['Tavan_South']=['P_Agri','P_Urban','P_Indust','P_Tour','P_Conserv']

        self.widgetCodes={}
        self.widgetCodes[("Zoning_North","Result")]="funcZoneDialog.lblZoneCodeValue"
        self.widgetCodes[("Zoning_North","Name")]="funcZoneDialog.lblZoneNameValue"
        self.widgetCodes[("Zoning_North","Regulation")]="funcZoneDialog.lblZoneNameValue"

        self.setWindowTitle(QApplication.translate("iczmDSS", "ICZM سیستم پشتیبان در تصمیم گیری برای", None, QApplication.UnicodeUTF8))
        self.resize(900, 700)
        self.setWindowState(Qt.WindowMaximized)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        #self.listView = QtGui.QListWidget(self.centralwidget)
        self.listView = TOCListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setResizeMode(QtGui.QListWidget.Adjust)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_2.addWidget(self.listView, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.map = MapnikWidget(self.groupBox)
        self.gridLayout.addWidget(self.map, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.lblX=QLabel(self.statusbar)
        self.lblY=QLabel(self.statusbar)
        self.lblX.setText(str(self.map.x))
        self.lblY.setText(str(self.map.y))
        #self.lbl.setGeometry(QtCore.QRect(self.statusbar.width() * 0.8, 5, 20, 20))
        self.statusbar.addPermanentWidget(self.lblX)
        self.statusbar.addPermanentWidget(self.lblY)
        self.listItems=[]

        #self.statusbar.addWidget(QLabel("Test2"))
        self.setStatusBar(self.statusbar)
        #gisToolbar = QToolBar(self)
        mapGroupActions=QActionGroup(self)
        txtZoomIn=QApplication.translate("Map", "بزرگنمایی", None, QApplication.UnicodeUTF8)
        self.zoomInAction=self.createAction(txtZoomIn,self.zoomIn,None,"zoomIn",txtZoomIn,True,"toggled(bool)")
        mapGroupActions.addAction(self.zoomInAction)

        txtZoomOut=QApplication.translate("Map", "کوچکنمایی", None, QApplication.UnicodeUTF8)
        self.zoomOutAction=self.createAction(txtZoomOut,self.zoomOut,None,"zoomOut",txtZoomOut,True,"toggled(bool)")
        mapGroupActions.addAction(self.zoomOutAction)

        txtPan=QApplication.translate("Map", "جابجایی نقشه", None, QApplication.UnicodeUTF8)
        self.PanAction=self.createAction(txtPan,self.pan,None,"pan",txtPan,True,"toggled(bool)")
        mapGroupActions.addAction(self.PanAction)

        txtIdentify=QApplication.translate("Map", "اطلاعات از عوارض", None, QApplication.UnicodeUTF8)
        self.IdentifyAction=self.createAction(txtIdentify,self.Identify,None,"identify",txtIdentify,True,"toggled(bool)")
        mapGroupActions.addAction(self.IdentifyAction)


        txtArrow=QApplication.translate("Map", "None", None, QApplication.UnicodeUTF8)
        self.ArrowAction=self.createAction(txtArrow,self.arrow,None,"cursor",txtArrow,True,"toggled(bool)")
        mapGroupActions.addAction(self.ArrowAction)

        txtZoomAll=QApplication.translate("Map", "نمایش کل وسعت نقشه", None, QApplication.UnicodeUTF8)
        self.ZoomAllAction=self.createAction(txtZoomAll,self.map.zoom_all,None,"earth",txtZoomAll)

        txtAddMap=QApplication.translate("Map", "باز کردن فایل لایه اطلاعاتی و اضافه کردن آن به نقشه", None, QApplication.UnicodeUTF8)
        self.addMapAction=self.createAction(txtAddMap,self.addLayerToMap,None,"add",txtAddMap)


        gisToolbar=self.addToolBar("GIS_Tools")
        gisToolbar.setObjectName("GIS_ToolBar")


        gisToolbar.addAction(self.addMapAction)
        gisToolbar.addAction(self.zoomInAction)
        gisToolbar.addAction(self.zoomOutAction)
        gisToolbar.addAction(self.PanAction)
        gisToolbar.addAction(self.IdentifyAction)
        gisToolbar.addAction(self.ArrowAction)
        gisToolbar.addAction(self.ZoomAllAction)

        #self.addToolBar(toolbar)
        gisToolbar.setIconSize(QSize(25,25))
        #self.map.addShapeSingleSymbole('Land_use.shp')


        model=TOCListModel(['landuse','agri','urban'],self.listView)
        self.identify=identifyDialog(self)
        #self.listView.itemClicked.connect(self.on_listWidget_itemClicked)
        self.listView.itemDoubleClicked.connect(self.changeMapColor)
        self.listView.itemChanged.connect(self.itemChanged)

        self.listView.itemMoved.connect(self.changeOrder)


        #################
        txtFzone=QApplication.translate("iczmDSS", "نمایش پهنه و ضابطه", None, QApplication.UnicodeUTF8)
        self.funcZoneAction=self.createAction(txtFzone,self.funcZone,"Ctrl+1","law",txtFzone)

        txtRisk=QApplication.translate("iczmDSS", "ارزیابی خطر", None, QApplication.UnicodeUTF8)
        self.riskAssessAction=self.createAction(txtRisk,self.funcRisk,"Ctrl+2","hazard",txtRisk)

        txtOpt=QApplication.translate("iczmDSS", "تهدیدها و فرصت های دریایی", None, QApplication.UnicodeUTF8)
        self.optAction=self.createAction(txtOpt,self.funcOpt,"Ctrl+3","sea",txtOpt)

        txtEcol=QApplication.translate("iczmDSS", "توان اکولوژیک", None, QApplication.UnicodeUTF8)
        self.ecologicAction=self.createAction(txtEcol,self.funcEcol,"Ctrl+4","ecology",txtEcol)

        fileMenu=self.menuBar().addMenu("&File")
#        self.addActions(dssMenu,(funcZoneAction,riskAssessAction,optAction,ecologicAction))

        dssMenu=self.menuBar().addMenu("&DSS")
        self.addActions(dssMenu,(self.funcZoneAction,self.riskAssessAction,self.optAction,self.ecologicAction))


        dssToolbar=self.addToolBar("DSS")
        dssToolbar.setObjectName("DSS_ToolBar")
        self.addActions(dssToolbar,(self.funcZoneAction,self.riskAssessAction,self.optAction,self.ecologicAction))
        dssToolbar.setIconSize(QSize(40,40))
        self.zoomSpinBox=QSpinBox()
        self.zoomSpinBox.setRange(1,400)
        self.zoomSpinBox.setSuffix(" %")
        self.zoomSpinBox.setValue(100)
        txtIconSize=QApplication.translate("iczmDSS", "اندازه آیتمها در نوار ابزار", None, QApplication.UnicodeUTF8)
        self.zoomSpinBox.setToolTip(txtIconSize)
        self.zoomSpinBox.setStatusTip(self.zoomSpinBox.toolTip())
        self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
        self.zoomSpinBox.valueChanged.connect(lambda: self.iconSize(dssToolbar))
        self.zoomSpinBox.valueChanged.connect(lambda: self.MapiconSize(gisToolbar))
        dssToolbar.addWidget(self.zoomSpinBox)

        helpMenu=self.menuBar().addMenu("&Help")
    #      self.addActions(dssMenu,(funcZoneAction,riskAssessAction,optAction,ecologicAction))

        txtAbout=QApplication.translate("iczmDSS", "راجع به نرم افزار", None, QApplication.UnicodeUTF8)
        self.AboutAction=self.createAction(txtAbout,self.About,None,"About",txtAbout)

        txtHFzone=QApplication.translate("iczmDSS", "راهنمای نمایش پهنه و ضبطه", None, QApplication.UnicodeUTF8)
        self.HfuncZoneAction=self.createAction(txtHFzone,self.HfuncZone,None,"Hlaw",txtHFzone)

        txtHRisk=QApplication.translate("iczmDSS", "راهنمای ارزیابی خطر", None, QApplication.UnicodeUTF8)
        self.HriskAssessAction=self.createAction(txtHRisk,self.HfuncRisk,None,"Hhazard",txtHRisk)

        txtHOpt=QApplication.translate("iczmDSS", "راهنمای تهدیدها و فرصت های دریایی", None, QApplication.UnicodeUTF8)
        self.HoptAction=self.createAction(txtHOpt,self.HfuncOpt,None,"Hsea",txtHOpt)

        txtHEcol=QApplication.translate("iczmDSS", "راهنمای توان اکولوژیک", None, QApplication.UnicodeUTF8)
        self.HecologicAction=self.createAction(txtHEcol,self.HfuncEcol,None,"Hecology",txtHEcol)

        txtHManual=QApplication.translate("iczmDSS", "راهنمای استفاده از نرم افزار", None, QApplication.UnicodeUTF8)
        self.HmanualAction=self.createAction(txtHManual,self.HManual,None,"About",txtHManual)

        txtHRef=QApplication.translate("iczmDSS", "باز کردن فایل مرجع ", None, QApplication.UnicodeUTF8)
        self.HrefAction=self.createAction(txtHRef,self.HRef,None,"About",txtHRef)

        self.addActions(helpMenu,(self.AboutAction, None, self.HfuncZoneAction,self.HriskAssessAction,self.HoptAction,self.HecologicAction,self.HmanualAction,self.HrefAction))

        txtExit=QApplication.translate("iczmDSS", "بستن نرم افزار", None, QApplication.UnicodeUTF8)
        self.CloseAction=self.createAction(txtExit,self.close,None,"close",txtExit)

        txtMapExport=QApplication.translate("iczmDSS", "...ذخیره نقشه در فایل", None, QApplication.UnicodeUTF8)
        self.mapExportAction=self.createAction(txtMapExport,self.exportMap,None,"saveMap",txtMapExport)

        txtPassCheck=QApplication.translate("iczmDSS", "!....ورود کلمه عبور", None, QApplication.UnicodeUTF8)
        self.passWordAction=self.createAction(txtPassCheck,self.passCheck,None,"password",txtPassCheck)
        #self.passWordAction.setCheckable(True)


        self.addActions(fileMenu,(self.mapExportAction,self.passWordAction,None,self.CloseAction))

        txtMap=QApplication.translate("iczmDSS", "نمایش اطلاعات مکانی", None, QApplication.UnicodeUTF8)
        mapAction=self.createAction(txtMap,self.mapShow,"Ctrl+M","Maps",txtMap)

        txtDssInfo=QApplication.translate("iczmDSS", "تعیین موقعیت مکانی برای استخراج اطلاعات سامانه پشتیبان تصمیم گیری", None, QApplication.UnicodeUTF8)
        self.DssInfoAction=self.createAction(txtDssInfo,self.dssInfoExtract,None,"dssInfo1",txtDssInfo,True,"toggled(bool)")
        mapGroupActions.addAction(self.DssInfoAction)
        mapToolbar=self.addToolBar("&Map")
        mapToolbar.setObjectName("Map_ToolBar")
        self.addActions(mapToolbar,(mapAction,self.DssInfoAction,None))
        mapToolbar.setIconSize(QSize(40,40))
        self.zoomSpinBox.valueChanged.connect(lambda: self.iconSize(mapToolbar))
        self.combo=QComboBox()
        f_settings=open('Settings/config.ini','r')
        lines=f_settings.readlines()
        f_settings.close()
        for l in lines:
            if l.split(':')[0].strip() == 'provinces':
                provList = l.split(':')[1].split(',')
                for prov in provList:
                    if prov.strip() == "Mazandaran":
                        txtCombo=QApplication.translate("iczmDSS", "مازندران", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "Golestan":
                        txtCombo=QApplication.translate("iczmDSS", "گلستان", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "Gilan":
                        txtCombo=QApplication.translate("iczmDSS", "گیلان", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "Khozestan":
                        txtCombo=QApplication.translate("iczmDSS", "خوزستان", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "Boushehr":
                        txtCombo=QApplication.translate("iczmDSS", "بوشهر", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "Hormozgan":
                        txtCombo=QApplication.translate("iczmDSS", "هرمزگان", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "Sistan":
                        txtCombo=QApplication.translate("iczmDSS", "سیستان و بلوچستان", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "North":
                        txtCombo=QApplication.translate("iczmDSS", "استانهای شمالی", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)
                    elif prov.strip() == "South":
                        txtCombo=QApplication.translate("iczmDSS", "استانهای جنوبی", None, QApplication.UnicodeUTF8)
                        self.combo.addItem(txtCombo)


        txtComboToolTip=QApplication.translate("iczmDSS", "تعیین محدوده در کشور برای نمایش نقشه", None, QApplication.UnicodeUTF8)
        self.combo.setToolTip(txtComboToolTip)
        self.combo.setStatusTip(self.combo.toolTip())

        txtReport=QApplication.translate("iczmDSS", "DSS تولید گزارش توسط", None, QApplication.UnicodeUTF8)
        self.reportAction=self.createAction(txtReport,self.report,"Ctrl+R","report",txtReport)
        mapToolbar.addAction(self.reportAction)
        mapToolbar.addWidget(self.combo)
        self.shouldClose=False
        self.activateDSSactions(False)


        if self.shouldPassWordCheck():
            self.frmPass=frmPassWord(self)
            self.frmPass.show()



    #mapnik.register_plugins('shape.input')
    def passCheck(self):
        self.frmPass=frmPassWord(self)
        self.frmPass.show()


    def updatePassCheckState(self,state):
        f=open('Settings/config.ini','r')
        lines=f.readlines()
        f.close()
        f=open('Settings/config.ini','w')
        p=False
        for l in lines:
            if l.split(':')[0].strip() == 'passCheck':
                p=True
                if state:
                    f.writelines(['passCheck: True'])
                else:
                    f.writelines(['passCheck: False'])
            else:
                f.writelines([l])
        if p:
            f.close()
        else:
            if state:
                f.writelines(['passCheck: True'])
            else:
                f.writelines(['passCheck: False'])

            f.close()

    def dssInfoExtract(self):
        if self.DssInfoAction.isChecked():
            QApplication.setOverrideCursor(QCursor(Qt.WhatsThisCursor))
            self.map.toolMode=11
        else:
            QApplication.restoreOverrideCursor()
    def shouldPassWordCheck(self):
        f=open('Settings/config.ini','r')
        lines=f.readlines()

        f.close()

        passCheck=True
        for l in lines:
            if l.split(':')[0].strip() == 'passCheck':
                if l.split(':')[1].strip() == 'True':

                    self.frmPass=frmPassWord(self)
                    self.frmPass.show()
                    passCheck=False
                else:
                    passCheck=False
        return passCheck

    def mapShow(self):
        if unicode(self.combo.currentText()) == 'گیلان'.decode('utf-8'):
            if self.selectedProvince !="_Gilan":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_Gilan"
                self.where=0
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_Gilan/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_Gilan/ManageB_Northc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                fname='Data/_Gilan/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])


                self.map.zoom_all()
        elif unicode(self.combo.currentText()) == 'مازندران'.decode('utf-8'):
            if self.selectedProvince !="_Mazandaran":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_Mazandaran"
                self.where=0
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_Mazandaran/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_Mazandaran/ManageB_Northc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                fname='Data/_Mazandaran/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                self.map.zoom_all()
        elif unicode(self.combo.currentText()) == 'گلستان'.decode('utf-8'):
            if self.selectedProvince !="_Golestan":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_Golestan"
                self.where=0
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_Golestan/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_Golestan/ManageB_North.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                fname='Data/_Golestan/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                self.map.zoom_all()
        elif unicode(self.combo.currentText()) == 'سیستان و بلوچستان'.decode('utf-8'):
            if self.selectedProvince !="_Sistan_Balouchestan":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_Sistan_Balouchestan"
                self.where=1
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_Sistan_Balouchestan/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_Sistan_Balouchestan/ManageB_Southc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                fname='Data/_Sistan_Balouchestan/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                self.map.zoom_all()
        elif unicode(self.combo.currentText()) == 'خوزستان'.decode('utf-8'):
            if self.selectedProvince !="_Khozestan":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_Khozestan"
                self.where=1
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_Khozestan/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_Khozestan/ManageB_Southc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                fname='Data/_Khozestan/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])


                self.map.zoom_all()
        elif unicode(self.combo.currentText()) == 'بوشهر'.decode('utf-8'):
            if self.selectedProvince !="_Boushehr":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_Boushehr"
                self.where=1
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_Boushehr/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_Boushehr/ManageB_Southc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                fname='Data/_Boushehr/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                self.map.zoom_all()
        elif unicode(self.combo.currentText()) == 'هرمزگان'.decode('utf-8'):
            if self.selectedProvince !="_Hormozgan":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_Hormozgan"
                self.where=1
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_Hormozgan/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_Hormozgan/ManageB_Southc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                fname='Data/_Hormozgan/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                self.map.zoom_all()

        elif unicode(self.combo.currentText()) == 'استانهای شمالی'.decode('utf-8'):
            if self.selectedProvince !="_North":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_North"
                self.where=0
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_North/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_North/ManageB_Northc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_North/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                self.map.zoom_all()
        elif unicode(self.combo.currentText()) == 'استانهای جنوبی'.decode('utf-8'):
            if self.selectedProvince !="_South":
                self.map.close_map()
                self.listView.clear()
                self.selectedProvince="_South"
                self.where=1
                self.Extracted=False
                self.activateDSSactions(False)
                if self.fZone:
                    self.funcZoneDialog.close()
                if self.fRisk:
                    self.formHazardDialog.close()
                if self.fOpt:
                    self.frmOptThreatDialog.close()
                if self.fEcol:
                    self.formEcologicDialog.close()

                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                fname='Data/_South/Province.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_South/ManageB_Southc.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                fname='Data/_South/Road.shp'.decode('utf-8')
                n=unicode.split(unicode.split(fname,"/")[-1],'.')
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])

                self.map.zoom_all()

    def activateDSSactions(self,active):
        if active:
            self.funcZoneAction.setEnabled(True)
            self.riskAssessAction.setEnabled(True)
            self.ecologicAction.setEnabled(True)
            self.optAction.setEnabled(True)
            self.reportAction.setEnabled(True)
        else:
            self.funcZoneAction.setEnabled(False)
            self.riskAssessAction.setEnabled(False)
            self.ecologicAction.setEnabled(False)
            self.optAction.setEnabled(False)
            self.reportAction.setEnabled(False)


    def iconSize(self,object,percent=None):
        if percent is None:
            percent = self.zoomSpinBox.value()
        size= 40 * percent / 100
        object.setIconSize(QSize(size,size))
    def MapiconSize(self,object,percent=None):
        if percent is None:
            percent = self.zoomSpinBox.value()
        size= 25 * percent / 100
        object.setIconSize(QSize(size,size))

    def addActions(self,target,actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


    def funcZone(self):
        if self.Extracted:
            self.funcZoneDialog=funcZoneDialog(self.where,self)
            self.funcZoneDialog.show()
            self.funcZoneDialog.setFixedSize(self.funcZoneDialog.size())
            self.fZone= True

        else:
            txtMapWarning=QApplication.translate("iczmDSS", "ابتدا لازم است موقعیت مکانی مورد نظر خود را بر روی نقشه تعیین نمایید", None, QApplication.UnicodeUTF8)
            txtMapWarningTitle=QApplication.translate("iczmDSS", "خطا", None, QApplication.UnicodeUTF8)
            QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)




    def funcRisk(self):
        if self.Extracted:
            self.formHazardDialog=formHazardDialog(self.where,self)
            self.formHazardDialog.show()
            self.formHazardDialog.setFixedSize( self.formHazardDialog.size())
            self.fRisk=True

        else:
            txtMapWarning=QApplication.translate("iczmDSS", "ابتدا لازم است موقعیت مکانی مورد نظر خود را بر روی نقشه تعیین نمایید", None, QApplication.UnicodeUTF8)
            txtMapWarningTitle=QApplication.translate("MainWindow", "خطا", None, QApplication.UnicodeUTF8)
            QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)



    def funcOpt(self):
        if self.Extracted:
            self.frmOptThreatDialog=frmOptThreatDialog(self.where,self)
            self.frmOptThreatDialog.show()
            self.frmOptThreatDialog.setFixedSize( self.frmOptThreatDialog.size())
            self.fOpt=True
        else:
            txtMapWarning=QApplication.translate("iczmDSS", "ابتدا لازم است موقعیت مکانی مورد نظر خود را بر روی نقشه تعیین نمایید", None, QApplication.UnicodeUTF8)
            txtMapWarningTitle=QApplication.translate("iczmDSS", "خطا", None, QApplication.UnicodeUTF8)
            QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)



    def funcEcol(self):
        if self.Extracted:
            self.formEcologicDialog=formEcologicDialog(self.where,self)
            self.formEcologicDialog.show()
            self.formEcologicDialog.setFixedSize( self.formEcologicDialog.size())
            self.fEcol=True
        else:
            txtMapWarning=QApplication.translate("iczmDSS", "ابتدا لازم است موقعیت مکانی مورد نظر خود را بر روی نقشه تعیین نمایید", None, QApplication.UnicodeUTF8)
            txtMapWarningTitle=QApplication.translate("iczmDSS", "خطا", None, QApplication.UnicodeUTF8)
            QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)

    def HfuncZone(self):
        if self.fHlp:
            self.hlp.webView.setUrl(QtCore.QUrl("Helps/functionalZone.html"))

        else:
            self.hlp=frmHelpView("Helps/functionalZone.html",self)
            self.hlp.show()
            self.fHlp=True



    def HfuncRisk(self):
        if self.fHlp:
            self.hlp.webView.setUrl(QtCore.QUrl("Helps/Hazard.html"))

        else:
            self.hlp=frmHelpView("Helps/Hazard.html",self)
            self.hlp.show()
            self.fHlp=True



    def HfuncOpt(self):
        if self.fHlp:
            self.hlp.webView.setUrl(QtCore.QUrl("Helps/Opt.html"))

        else:
            self.hlp=frmHelpView("Helps/Opt.html",self)
            self.hlp.show()
            self.fHlp=True



    def HfuncEcol(self):
        if self.fHlp:
            self.hlp.webView.setUrl(QtCore.QUrl("Helps/ecologic.html"))

        else:
            self.hlp=frmHelpView("Helps/ecologic.html",self)
            self.hlp.show()
            self.fHlp=True
    def HRef(self):
        os.startfile('Helps\\ICZM_DSS-Reference.pdf')

    def HManual(self):
        if self.fHlp:
            self.hlp.webView.setUrl(QtCore.QUrl("Helps/ICZM_DSS_manual.html"))

        else:
            self.hlp=frmHelpView("Helps/ICZM_DSS_manual.html",self)
            self.hlp.show()
            self.fHlp=True

    def About(self):
        if self.fHlp:
            self.hlp.webView.setUrl(QtCore.QUrl("Helps/ICZM_Main.html"))

        else:
            self.hlp=frmHelpView("Helps/ICZM_Main.html",self)
            self.hlp.show()
            self.fHlp=True
    def HazardDecode(self,value):
        hazard='-'
        if value == 0:
            hazard='فاقد خطر'
        elif value == 1:
            hazard='خطر کم'
        elif value == 2:
            hazard='خطر متوسط'
        elif value == 3:
            hazard='خطر زیاد'
        return hazard

    def OptDecode(self,value):
        Opt='-'
        if value == 0:
            Opt='بی اثر'
        elif value == 1:
            Opt='کم'
        elif value == 2:
            Opt='متوسط'
        elif value == 3:
            Opt='زیاد'
        return Opt

    def report(self):
        titles=['پهنه بندی عملکردی','مرز مدیریتی','مخاطرات','فرضتهای دریایی','تهدیدهای دریایی','توان اکولوژیک']
        if self.where == 0:
            t1=OrderedDict()
            t1["عنوان"]="مقدار"
            t1["کد پهنه"]=str(self.Result[("Zoning_North","Result")])
            t1["نام پهنه"]=str(self.Result[("Zoning_North","Name")])
            t2=OrderedDict()
            t2["عنوان"]="مقدار"
            t2["توضیحات"]=str(self.Result[("ManageB_North","name")])
            t2["ضوابط"]=str(self.Result[("ManageB_North","MC")])
            t3=OrderedDict()
            t3['نوع مخاطره']='میزان خطر'
            t3['باران']=self.HazardDecode(self.Result[("Hazards_North","R")])
            t3['زلزله']=self.HazardDecode(self.Result[("Hazards_North","Q")])
            t3['رانش']=self.HazardDecode(self.Result[("Hazards_North","L")])
            t3['سیل']=self.HazardDecode(self.Result[("Hazards_North","F")])
            t3['یخبندان']=self.HazardDecode(self.Result[("Hazards_North","I")])
            t3['خشنسالی']=self.HazardDecode(self.Result[("Hazards_North","K")])
            t3['طوفان']=self.HazardDecode(self.Result[("Hazards_North","S")])
            t4=OrderedDict()
            t4['بخش']='میزان'
            t4['گردشگری']=self.OptDecode(self.Result[("Opportunity_North","O_Tour")])
            t4['صنعتی']=self.OptDecode(self.Result[("Opportunity_North","O_Indust")])
            t4['سکونت']=self.OptDecode(self.Result[("Opportunity_North","O_Resid")])
            t4['کشاورزی']=self.OptDecode(self.Result[("Opportunity_North","O_Agri")])
            t5=OrderedDict()
            t5['بخش']='میزان'
            t5['گردشگری']=self.OptDecode(self.Result[("Threat_North","T_Tour")])
            t5['صنعتی']=self.OptDecode(self.Result[("Threat_North","T_Indust")])
            t5['سکونت']=self.OptDecode(self.Result[("Threat_North","T_Resid")])
            t5['کشاورزی']=self.OptDecode(self.Result[("Threat_North","T_Agri")])
            t6=OrderedDict()
            t6['کاربری']='توان'
            t6['کشاورزی']=str(self.Result[("Tavan_North","P_Agri")])
            t6['گردشگری']=str(self.Result[("Tavan_North","P_Tour")])
            t6['صنعتی']=str(self.Result[("Tavan_North","P_Indust")])
            t6['حفاظتی']=str(self.Result[("Tavan_North","P_Conserv")])
            t6['شهری']=str(self.Result[("Tavan_North","P_Urban")])

        else:
            t1=OrderedDict()
            t1["عنوان"]="مقدار"
            t1["کد پهنه"]=str(self.Result[("Zoning_South","Result")])
            t1["نام پهنه"]=str(self.Result[("Zoning_South","Name")])
            t2=OrderedDict()
            t2["عنوان"]="مقدار"
            t2["توضیحات"]=str(self.Result[("ManageB_South","Name")])
            t2["ضوابط"]=str(self.Result[("ManageB_South","MC")])
            t3=OrderedDict()
            t3['نوع مخاطره']='میزان خطر'
            t3['باران']=self.HazardDecode(self.Result[("Hazards_South","R")])
            t3['زلزله']=self.HazardDecode(self.Result[("Hazards_South","Q")])
            t3['رانش']=self.HazardDecode(self.Result[("Hazards_South","L")])
            t3['خشنسالی']=self.HazardDecode(self.Result[("Hazards_South","K")])
            t3['طوفان']=self.HazardDecode(self.Result[("Hazards_South","S")])
            t4=OrderedDict()
            t4['بخش']='میزان'
            t4['گردشگری']=self.OptDecode(self.Result[("Opportunity_South","O_Tour")])
            t4['صنعتی']=self.OptDecode(self.Result[("Opportunity_South","O_Indust")])
            t4['سکونت']=self.OptDecode(self.Result[("Opportunity_South","O_Resid")])
            t4['کشاورزی']=self.OptDecode(self.Result[("Opportunity_South","O_Agri")])
            t5=OrderedDict()
            t5['بخش']='میزان'
            t5['گردشگری']=self.OptDecode(self.Result[("Threat_South","T_Tour")])
            t5['صنعتی']=self.OptDecode(self.Result[("Threat_South","T_Indust")])
            t5['سکونت']=self.OptDecode(self.Result[("Threat_South","T_Resid")])
            t5['کشاورزی']=self.OptDecode(self.Result[("Threat_South","T_Agri")])
            t6=OrderedDict()
            t6['کاربری']='توان'
            t6['کشاورزی']=str(self.Result[("Tavan_South","P_Agri")])
            t6['گردشگری']=str(self.Result[("Tavan_South","P_Tour")])
            t6['صنعتی']=str(self.Result[("Tavan_South","P_Indust")])
            t6['حفاظتی']=str(self.Result[("Tavan_South","P_Conserv")])
            t6['شهری']=str(self.Result[("Tavan_South","P_Urban")])

        #self.MapRenderToFile('temp/map.png')
        self.MapRenderToFile('temp/'+self.reportName)

        self.generateHTML(unicode(self.combo.currentText()).encode('utf-8'),[self.x,self.y],[t1,t2,t3,t4,t5,t6],titles)
        if self.fHlp:
            self.hlp.webView.setUrl(QtCore.QUrl("temp/report.html"))
            #self.hlp.webView.reload()

        else:

            self.hlp=frmHelpView("",self)
            self.hlp.destroy()
            self.hlp=frmHelpView("",self)
            self.hlp.show()
            self.hlp.webView.setUrl(QtCore.QUrl("temp/report.html"))
            self.hlp.webView.reload()


            self.fHlp=True



    def generateHTML(self,province,coordinates,tables=[],tableTitles=[]):
        f=open('Settings/frp','r')
        l=f.readlines()
        f.close()
        fs=open('temp/report.html','w')
        for line in l:
            fs.writelines([line])
        fs.writelines(['<body>\n<div style="text-align: center; font-family: Tahoma;">\n<h2 style="color: rgb(153, 0, 0);">\n'])
        fs.writelines(['گزارش تولید شده توسط نرم افزار سامانه پشتیبان تصمیم گیری برای مدیریت یکپارچه مناطق ساحلی'])
        fs.writelines(['\n</h2><img style="width: 150px; height: 112px;" alt="" src="../Icons/logo.png">\n</div>\n'])

        fs.writelines(['<div style="text-align: right;font-family: Tahoma;">\n'])

        fs.writelines(['<hr style="width: 100%; height: 2px;">\n<br>\n'])
        fs.writelines(['استان انتخابی  : ','<span style="color: rgb(0, 0, 102); text-decoration: underline; font-weight: bold;">',province,'</span>\n<br><br>\n'])

        fs.writelines([': مختصات محل انتخاب شده برای استخراج اطلاعات و تولید این گزارش'+ '\n<br><br>'])

        fs.writelines(['<table style="width: 732px; height: 115px; text-align: center; margin-left: auto; margin-right: 50px;" border="2" cellpadding="2" cellspacing="2">'])
        fs.writelines(['<tbody>\n<tr style="font-weight: bold; background-color: rgb(204, 204, 255);">\n<td>"Y"</td><td>"X"</td>\n</tr>\n'])
        fs.writelines(['<tr>\n<td>',str(coordinates[1]),'</td><td>',str(coordinates[0]),'</td>\n</tr>\n</tbody>\n</table>\n<br><br>\n'])

        fs.writelines([':نقشه ذیل موقعیت محدوده به همراه نقطه انتخابی نمایش می دهد','\n<br><br>'])
        #fs.writelines(['<div style="text-align: center;">\n<img style="border: 1px solid ; width: 900px; height: 567px;" alt="" src="map.png" align="top"><br>\n</div><br><br>\n'])
        fs.writelines(['<div style="text-align: center;">\n<img style="border: 1px solid ; width: 900px; height: 567px;" alt="" src="',self.reportName,'" align="top"><br>\n</div><br><br>\n'])

        for i in range(len(tables)):
            tbl=tables[i]
            fs.writelines(['نمایش اطلاعات مربوط به ','<span style="color: rgb(0, 0, 102); text-decoration: underline; font-weight: bold;">',tableTitles[i],'</span>\n<br><br>\n'])
            fs.writelines(['<table style="width: 732px; height: 115px; text-align: center; margin-left: auto; margin-right: 50px;" border="2" cellpadding="2" cellspacing="2"><tbody>\n'])
            fs.writelines(['<tr style="font-weight: bold; background-color: rgb(204, 204, 255);">\n<td>',tbl[tbl.keys()[0]],'</td><td>',tbl.keys()[0],'</td>\n</tr>\n'])
            for k in tbl.keys()[1:]:
                fs.writelines(['<tr>\n<td>',tbl[k],'</td><td>',k,'</td>\n</tr>\n'])
            fs.writelines(['</tbody>\n</table>\n<br><br>\n'])

        fs.writelines(['<hr style="width: 100%; height: 2px;">\n<br>\n'])
        fs.writelines(['<small>','این گزارش توسط نرم افزار سامانه پشتیبان تصمیم گیری برای مدیریت یکپارچه مناطق ساحلی تولید شده است','</small><br>\n'])
        fs.writelines(['<small>','نرم افزار فوق توسط ','<span style="color: rgb(0, 0, 102); text-decoration: underline; font-weight: bold;">','اداره کل مهندسی سواحل و بنادر، معاونت توسعه و تجهیز بنادر سازمان بنادر و دریانوردی ','</span>','توسعه داده شده است','</small>'])
        fs.writelines(['</div>\n</body>\n</html>'])
        fs.close()

    #############
    def changeOrder(self):
        lyrs=[lyr.name for lyr in self.map.map.layers]
        items=[unicode(self.listView.item(i).text()).encode('utf-8') for i in range(self.listView.count())]
        newIndex=[]

        for i in range(len(items)):
            newIndex.append(lyrs.index(items[i]))

        self.map.mapLayerOrderChange(newIndex)
        self.map.updateMap()






    def changeMapColor(self):

        n=unicode(self.listView.currentItem().text())

        if self.map.mapLayers[n] in ["Polygon", "MultiPolygon"]:
            clr = QColorDialog.getColor()
            if str(clr.name()) != '#000000':
                self.map.map.remove_style(n.encode('utf-8'))
                polyS=self.map.singlePolyStyle(str(clr.name()))
                self.map.map.append_style(n.encode('utf-8'),polyS)
                self.listView.currentItem().setData(Qt.DecorationRole, QVariant(clr))
                self.map.updateMap()
        elif self.map.mapLayers[n] in ["LineString", "MultiLineString","Line"]:
            clr = QColorDialog.getColor()
            if str(clr.name()) != '#000000':
                self.map.map.remove_style(n.encode('utf-8'))
                lineS=self.map.singleLineStyle(str(clr.name()),0.5)
                self.map.map.append_style(n.encode('utf-8'),lineS)
                self.map.updateMap()


    def itemChanged(self,item):
        rev=range(self.listView.count())
        rev.reverse()
        rev=rev[self.listView.indexFromItem(item).row()]

        if item.checkState() == Qt.Checked:
            self.map.map.layers[rev].active=True
            self.map.updateMap()
        else:
            self.map.map.layers[rev].active=False
            self.map.updateMap()

    def on_listWidget_itemClicked(self, item):
        print item.text()
        #if item.listWidget().itemWidget(item) != None:
        if item.checkState() == Qt.Checked:
            #item.setCheckState(Qt.Unchecked)
            #self.map.map.layers[self.]
            print "ii"
            print self.listView.indexFromItem(item).row()
        else:
            #item.setCheckState(Qt.Checked)
            print "unchecked"

    def addLayerToMap(self):
        txtOpenFile=QApplication.translate("iczmDSS", "اضافه کردن لایه به نقشه", None, QApplication.UnicodeUTF8)
        file_type="Shape_files (*.shp)"
        fname = unicode(QtGui.QFileDialog.getOpenFileName(self, txtOpenFile,self.lastOpenPath(),file_type))
        if fname != "":
            self.updateLastOpenPath(fname.rsplit("/",1)[0].encode('utf-8'))
            n=unicode.split(unicode.split(fname,"/")[-1],'.')
            if (n[-1].lower() == 'shp'):
                addState = self.map.addShapeSingleSymbole(fname,name=n[0].encode('utf-8'))
                self.itemGenerate([addState[0].decode('utf-8')],[addState[1]],[addState[2]])
                self.map.zoom_all()
            elif (n[0].lower() != ''):
                txtMapWarning=QApplication.translate("iczmDSS", "فایل با پسوند مناسب برای اضافه شدن به نقشه انتخاب نشده است...", None, QApplication.UnicodeUTF8)
                txtMapWarningTitle=QApplication.translate("iczmDSS", "خطا", None, QApplication.UnicodeUTF8)
                QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)




    def createAction(self,text,slot=None,shortcut=None,icon=None,tip=None,checkable=False,signal="triggered()"):
        action=QAction(text,self)
        if icon is not None:
            action.setIcon(QIcon("Icons/%s.png" %icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action,SIGNAL(signal),slot)
        if checkable:
            action.setCheckable(True)
        return action
    def zoomIn(self):
        if self.zoomInAction.isChecked():
            QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
            self.map.toolMode=1
        else:
            QApplication.restoreOverrideCursor()

    def zoomOut(self):
        if self.zoomOutAction.isChecked():
            QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
            self.map.toolMode=2
        else:
            QApplication.restoreOverrideCursor()
    def pan(self):
        if self.PanAction.isChecked():
            QApplication.setOverrideCursor(QCursor(Qt.OpenHandCursor))
            self.map.toolMode=3
        else:
            QApplication.restoreOverrideCursor()
    def Identify(self):
        if self.IdentifyAction.isChecked():
            QApplication.setOverrideCursor(QCursor(Qt.WhatsThisCursor))
            self.map.toolMode=4
        else:
            QApplication.restoreOverrideCursor()

    def arrow(self):
        if self.ArrowAction.isChecked():
            QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))
            self.map.toolMode=0
        else:
            QApplication.restoreOverrideCursor()

    def itemGenerate(self,data=[],color=[],geomType=[]):
        for i in range(len(data)):
            item = QListWidgetItem()

            if geomType[i] in ["Point", "MultiPoint"]:
                item.setData(Qt.DecorationRole, QPixmap("Icons/point_s.png"))
            elif geomType[i] in ["LineString", "MultiLineString","Line"]:
                item.setData(Qt.DecorationRole, QPixmap("Icons/line_s.png"))

            else:
                item.setData(Qt.DecorationRole, QVariant(QColor(color[i])))


            item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled| Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
            item.setText(data[i])
            item.setCheckState(2)
            self.listView.insertItem(0,item)

    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Delete:
            r = self.listView.currentIndex().row()
            if r != -1:
                item = self.listView.takeItem(self.listView.currentRow())
                self.listView.removeItemWidget(item)
                self.map.map.layers.__delitem__(len(self.map.map.layers)-1-r)
                self.map.updateMap()
                self.listView.update()

    def readSpatialData(self,filenames,specialfiles,x,y):
        out={}
        driver = ogr.GetDriverByName('ESRI Shapefile')
        p=ogr.Geometry(ogr.wkbPoint)
        p.AddPoint(x,y)
        for f in filenames:
            ds = driver.Open("Data/"+self.selectedProvince+"/"+f+'.shp',0)
            layer = ds.GetLayer()
            layer.SetSpatialFilter(p)
            layer.ResetReading()
            feature=layer.GetNextFeature()
            for fld in self.FieldNames[f]:
                try:
                    out[(f,fld)]=feature.GetField(fld)
                except:
                    out[(f,fld)]=0

        for f in specialfiles:
            if str(out[(f,'Code')]) <> '0':
                fsp = open("Data/"+self.selectedProvince+"/"+f+".txt", 'r')
                mtx = [line.rstrip().split(',') for line in fsp.readlines()]
                fsp.close()
                v=[line[0] for line in mtx[1:]]
                oID = v.index(str(out[(f,'Code')]))
                oID+=1
                for fld in self.FieldNames[f][:-1]:
                    fID=mtx[0].index(fld)
                    out[(f,fld)]=mtx[oID][fID]
        return out

    def extractData(self,where):
        if (len(self.map.map.layers) > 0):
            j=1000
            for i in range(0,len(self.map.map.layers)):
                if (self.map.map.layers[i].name == 'Selected_Location'):
                    j=i
            if (j <> 1000):

                item = self.listView.takeItem(len(self.map.map.layers)-1-j)
                self.map.map.layers.__delitem__(j)
                self.listView.removeItemWidget(item)
                self.map.updateMap()
                self.listView.update()
                j=1000
        if where == 0:
            self.Result = self.readSpatialData(self.North_Files,self.North_SpecialFiles,self.x,self.y)



            if str(self.Result[("Zoning_North","Code")]) <> '0':
                self.Extracted=True
                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo2.png"))
                self.activateDSSactions(True)
                self.reportName='reportMap_'+self.selectedProvince+'.png'
                #######
                ds = mapnik.MemoryDatasource()
                wkt = 'Point ('+str(self.x)+' '+str(self.y)+')'
                f = mapnik.Feature(mapnik.Context(),1)
                f.add_geometries_from_wkt(wkt)
                ds.add_feature(f)
                lyr = mapnik.Layer("Selected_Location")
                lyr.datasource = ds
                s=self.map.singlePointStyle(mapnik.PathExpression("Icons/map_point.png"),0.2)
                prj=self.map.map.srs
                lyr.srs=prj
                self.map.map.append_style("Selected_Location",s)
                lyr.styles.append("Selected_Location")
                self.map.map.layers.append(lyr)
                self.map.mapLayers["Selected_Location"]="Point"
                self.map.updateMap()

                item = QListWidgetItem()
                item.setData(Qt.DecorationRole, QPixmap("Icons/map_point2.png"))
                item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled| Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                item.setText("Selected_Location")
                item.setCheckState(2)
                self.listView.insertItem(0,item)

            else:
                self.Extracted=False
                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                self.activateDSSactions(False)
                self.reportName=''
        else:
            self.Result = self.readSpatialData(self.South_Files,self.South_SpecialFiles,self.x,self.y)

            if str(self.Result[("Zoning_South","Code")]) <> '0':
                self.Extracted=True
                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo2.png"))
                self.activateDSSactions(True)
                self.reportName='reportMap_'+self.selectedProvince+'.png'
                 #######
                ds = mapnik.MemoryDatasource()
                wkt = 'Point ('+str(self.x)+' '+str(self.y)+')'
                f = mapnik.Feature(mapnik.Context(),1)
                f.add_geometries_from_wkt(wkt)
                ds.add_feature(f)
                lyr = mapnik.Layer("Selected_Location")
                lyr.datasource = ds
                s=self.map.singlePointStyle(mapnik.PathExpression("Icons/map_point.png"),0.2)
                prj=self.map.map.srs
                lyr.srs=prj
                self.map.map.append_style("Selected_Location",s)
                lyr.styles.append("Selected_Location")
                self.map.map.layers.append(lyr)
                self.map.mapLayers["Selected_Location"]="Point"
                self.map.updateMap()

                item = QListWidgetItem()
                item.setData(Qt.DecorationRole, QPixmap("Icons/map_point2.png"))
                item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled| Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                item.setText("Selected_Location")
                item.setCheckState(2)
                self.listView.insertItem(0,item)

            else:
                self.Extracted=False
                self.DssInfoAction.setIcon(QIcon("Icons/dssInfo1.png"))
                self.activateDSSactions(False)
                self.reportName=''
    def exportMap(self):
        txtSaveFile=QApplication.translate("iczmDSS", "ذخیره نقشه در فایل", None, QApplication.UnicodeUTF8)
        file_type="png (*.png);; svg (*.svg);; jpeg (*.jpg);; pdf (*.pdf)"
        fname = unicode(QtGui.QFileDialog.getSaveFileName(self, txtSaveFile,'',file_type))
        n=unicode.split(unicode.split(fname,"/")[-1],'.')
        n=str(n[-1].lower())
        if n == 'jpg':
            n='jpeg'

        fname=fname.encode('utf-8')
        n=n.encode('utf-8')
        self.MapRenderToFile(fname,n)

    def MapRenderToFile(self,filename,Format='png'):
        mapnik.render_to_file(self.map.map,filename,Format)

    def lastOpenPath(self):
        path=""
        if os.path.exists('Settings/config.ini'):
            f=open('Settings/config.ini','r')
            lines=f.readlines()
            f.close()
            for l in lines:
                if l.split(':')[0].strip() == 'lastOpenPath':
                    path=str(l.split(':',1)[1].strip())
        return path
    def updateLastOpenPath(self,newPath):
        if os.path.exists('Settings/config.ini'):
            f=open('Settings/config.ini','r')
            lines=f.readlines()
            f.close()
            f=open('Settings/config.ini','w')
            for l in lines:
                if l.split(':')[0].strip() == 'lastOpenPath':
                    f.writelines(['lastOpenPath: ',newPath,'\n'])
                else:
                    f.writelines([l])
            f.close()



def main():
    app=QApplication([])
    app.setOrganizationName("Sap Consulting Engineers Co.")
    app.setOrganizationDomain("r-gis.net")
    app.setApplicationName("ICZM DSS")
    app.setWindowIcon(QIcon("Icons/iczm.png"))


    w=iczmDSS()
    pixmap = QPixmap("Icons/splash.png")
    splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
    splash.setMask(pixmap.mask()) # this is usefull if the splashscreen is
    progressBar = QProgressBar(splash)
    progressBar.setGeometry(splash.width()/20, 8*splash.height()/8.5, 8*splash.width()/15, splash.height()/25)

    splash.show()

    for i in range(0, 101):
       progressBar.setValue(i)

    # Do something which takes some time.
       t = time.time()
       while time.time() < t + 0.03:
            app.processEvents()
    #for i in range(0,20000):
        #if i % 5 == 0: splash.showMessage(''.join([ "=" for n in range(i/200)]), Qt.AlignLeft | Qt.AlignBottom, Qt.red)
     #   if i % 5 == 0: pass
  #  time.sleep(1)
    #splash.showMessage((u'Starting...'), Qt.AlignRight | Qt.AlignBottom, Qt.yellow)
        # make sure Qt really display the splash screen
    app.processEvents()
    w.show()
        # start tha main app window
    w.raise_()
    splash.finish(w)

    #w.load_map(sys.argv[1])
    #w.load_map()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()