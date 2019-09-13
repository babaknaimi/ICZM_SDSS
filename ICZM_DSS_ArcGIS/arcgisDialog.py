# -*- coding: utf-8 -*-

# ICZM DSS
# standalone software, to be linked to ArcGIS
# Created:
#      by: Babak Naimi
#           naimi.b@gmail.com


from PyQt4 import QtCore, QtGui
from formTextBrowser import *
import sip, sys
import osgeo.ogr as ogr
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class arcgisDialog(QtGui.QDialog):
    def __init__(self,path,where,province,x,y,parent=None):
        super(arcgisDialog,self).__init__(parent)

        self.x=x
        self.y=y
        self.Extracted=False
        self.selectedProvince=province
        self.where=where
        self.path=path


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



        self.extractData(self.where)

        self.setObjectName(_fromUtf8("ICZMDSS_ArcGIS"))
        self.setFixedSize(QtCore.QSize(722, 695))
        #self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.setFocus()
        col1 = QtGui.QColor(207, 209, 154)
        col2 = QtGui.QColor(236, 238, 176)
        col3 = QtGui.QColor(213, 255, 215)
        col4 = QtGui.QColor(230, 217, 255)
        col5 = QtGui.QColor(255, 245, 231)
        col6 = QtGui.QColor(254, 251, 136)
        self.setStyleSheet("QDialog { background-color: %s }" % col1.name())

        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        self.setFont(font)
        self.setModal(False)
        pixmap=QtGui.QPixmap("Icons/iczm_img1.png")
        self.lbl = QtGui.QLabel(self.tab)
        self.lbl.setGeometry(QtCore.QRect(1, 20, 240, 620))
        self.lbl.setObjectName(_fromUtf8("graphicsView"))
        self.lbl.setScaledContents(True)
        self.lbl.setPixmap(pixmap)
        self.groupBox1 = QtGui.QGroupBox(self.tab)
        self.groupBox1.setGeometry(QtCore.QRect(250, 3, 440, 121))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.groupBox1.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.widget = QtGui.QWidget(self.groupBox1)
        self.widget.setGeometry(QtCore.QRect(12, 22, 425, 91))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblZoneCode = QtGui.QLabel(self.widget)
        self.lblZoneCode.setAlignment(QtCore.Qt.AlignCenter)
        self.lblZoneCode.setObjectName(_fromUtf8("lblZoneCode"))
        self.lblZoneCode.setStyleSheet("QLabel { background-color: %s }" % col6.name())

        self.horizontalLayout.addWidget(self.lblZoneCode)
        self.lblZoneName = QtGui.QLabel(self.widget)
        self.lblZoneName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblZoneName.setObjectName(_fromUtf8("lblZoneName"))
        self.lblZoneName.setStyleSheet("QLabel { background-color: %s }" % col6.name())

        self.horizontalLayout.addWidget(self.lblZoneName)
        self.lblLaws = QtGui.QLabel(self.widget)
        self.lblLaws.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLaws.setObjectName(_fromUtf8("lblLaws"))
        self.lblLaws.setStyleSheet("QLabel { background-color: %s }" % col6.name())

        self.horizontalLayout.addWidget(self.lblLaws)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblZoneCodeValue = QtGui.QLabel(self.widget)
        self.lblZoneCodeValue.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lblZoneCodeValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblZoneCodeValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblZoneCodeValue.setLineWidth(1)
        self.lblZoneCodeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblZoneCodeValue.setObjectName(_fromUtf8("lblZoneCodeValue"))
        self.lblZoneCodeValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.horizontalLayout_2.addWidget(self.lblZoneCodeValue)
        self.lblZoneNameValue = QtGui.QLabel(self.widget)
        self.lblZoneNameValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblZoneNameValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblZoneNameValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblZoneNameValue.setObjectName(_fromUtf8("lblZoneNameValue"))
        self.lblZoneNameValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.horizontalLayout_2.addWidget(self.lblZoneNameValue)
        self.bottonLaws = QtGui.QPushButton(self.widget)
        self.bottonLaws.setObjectName(_fromUtf8("bottonLaws"))
        self.horizontalLayout_2.addWidget(self.bottonLaws)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox2 = QtGui.QGroupBox(self.tab)
        self.groupBox2.setGeometry(QtCore.QRect(250, 121, 440, 261))
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.groupBox2.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.widget1 = QtGui.QWidget(self.groupBox2)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 425, 20))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblDetails = QtGui.QLabel(self.widget1)
        self.lblDetails.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDetails.setObjectName(_fromUtf8("lblDetails"))
        self.lblDetails.setStyleSheet("QLabel { background-color: %s }" % col6.name())

        self.horizontalLayout_3.addWidget(self.lblDetails)
        self.lblManageLaws = QtGui.QLabel(self.widget1)
        self.lblManageLaws.setAlignment(QtCore.Qt.AlignCenter)
        self.lblManageLaws.setObjectName(_fromUtf8("lblManageLaws"))
        self.lblManageLaws.setStyleSheet("QLabel { background-color: %s }" % col6.name())

        self.horizontalLayout_3.addWidget(self.lblManageLaws)
        self.widget2 = QtGui.QWidget(self.groupBox2)
        self.widget2.setGeometry(QtCore.QRect(10, 50, 425, 201))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lblDetailsValue = QtGui.QLabel(self.widget2)
        self.lblDetailsValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblDetailsValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDetailsValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDetailsValue.setWordWrap(True)
        self.lblDetailsValue.setObjectName(_fromUtf8("lblDetailsValue"))
        self.lblDetailsValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.horizontalLayout_4.addWidget(self.lblDetailsValue)
        self.lblManageLawsValue = QtGui.QLabel(self.widget2)
        self.lblManageLawsValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblManageLawsValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblManageLawsValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblManageLawsValue.setWordWrap(True)
        self.lblManageLawsValue.setObjectName(_fromUtf8("lblManageLawsValue"))
        self.lblManageLawsValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.horizontalLayout_4.addWidget(self.lblManageLawsValue)
        self.groupBox3 = QtGui.QGroupBox(self.tab)
        self.groupBox3.setGeometry(QtCore.QRect(250, 376, 440, 301))
        self.groupBox3.setObjectName(_fromUtf8("groupBox3"))
        self.groupBox3.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.lblHazards = QtGui.QLabel(self.groupBox3)
        self.lblHazards.setGeometry(QtCore.QRect(6, 20, 149, 233))
        self.lblHazards.setFrameShape(QtGui.QFrame.Panel)
        self.lblHazards.setFrameShadow(QtGui.QFrame.Raised)
        self.lblHazards.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHazards.setObjectName(_fromUtf8("lblHazards"))
        self.lblHazards.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblRain = QtGui.QLabel(self.groupBox3)
        self.lblRain.setGeometry(QtCore.QRect(156, 20, 139, 31))
        self.lblRain.setFrameShape(QtGui.QFrame.Box)
        self.lblRain.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblRain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRain.setObjectName(_fromUtf8("lblRain"))
        self.lblRain.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblEarthquake = QtGui.QLabel(self.groupBox3)
        self.lblEarthquake.setGeometry(QtCore.QRect(156, 53, 139, 31))
        self.lblEarthquake.setFrameShape(QtGui.QFrame.Box)
        self.lblEarthquake.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblEarthquake.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEarthquake.setObjectName(_fromUtf8("lblEarthquake"))
        self.lblEarthquake.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblLandslide = QtGui.QLabel(self.groupBox3)
        self.lblLandslide.setGeometry(QtCore.QRect(156, 86, 139, 31))
        self.lblLandslide.setFrameShape(QtGui.QFrame.Box)
        self.lblLandslide.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblLandslide.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLandslide.setObjectName(_fromUtf8("lblLandslide"))
        self.lblLandslide.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblFlood = QtGui.QLabel(self.groupBox3)
        self.lblFlood.setGeometry(QtCore.QRect(156, 122, 139, 31))
        self.lblFlood.setFrameShape(QtGui.QFrame.Box)
        self.lblFlood.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblFlood.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFlood.setObjectName(_fromUtf8("lblFlood"))
        self.lblFlood.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblIce = QtGui.QLabel(self.groupBox3)
        self.lblIce.setGeometry(QtCore.QRect(156, 157, 139, 31))
        self.lblIce.setFrameShape(QtGui.QFrame.Box)
        self.lblIce.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIce.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIce.setObjectName(_fromUtf8("lblIce"))
        self.lblIce.setStyleSheet("QLabel { background-color: %s }" % col4.name())


        self.lblDrought = QtGui.QLabel(self.groupBox3)
        self.lblDrought.setGeometry(QtCore.QRect(156, 190, 139, 31))
        self.lblDrought.setFrameShape(QtGui.QFrame.Box)
        self.lblDrought.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDrought.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDrought.setObjectName(_fromUtf8("lblDrought"))
        self.lblDrought.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblTunder = QtGui.QLabel(self.groupBox3)
        self.lblTunder.setGeometry(QtCore.QRect(156, 223, 139, 31))
        self.lblTunder.setFrameShape(QtGui.QFrame.Box)
        self.lblTunder.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTunder.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTunder.setObjectName(_fromUtf8("lblTunder"))
        self.lblTunder.setStyleSheet("QLabel { background-color: %s }" % col4.name())


        self.lblRainValue = QtGui.QLabel(self.groupBox3)
        self.lblRainValue.setGeometry(QtCore.QRect(296, 20, 138, 31))
        self.lblRainValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblRainValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblRainValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRainValue.setObjectName(_fromUtf8("lblRainValue"))
        self.lblRainValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblEarthquakeValue = QtGui.QLabel(self.groupBox3)
        self.lblEarthquakeValue.setGeometry(QtCore.QRect(296, 53, 138, 31))
        self.lblEarthquakeValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblEarthquakeValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblEarthquakeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEarthquakeValue.setObjectName(_fromUtf8("lblEarthquakeValue"))
        self.lblEarthquakeValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblLandslideValue = QtGui.QLabel(self.groupBox3)
        self.lblLandslideValue.setGeometry(QtCore.QRect(296, 86, 138, 31))
        self.lblLandslideValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblLandslideValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblLandslideValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLandslideValue.setObjectName(_fromUtf8("lblLandslideValue"))
        self.lblLandslideValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblFloodValue = QtGui.QLabel(self.groupBox3)
        self.lblFloodValue.setGeometry(QtCore.QRect(296, 122, 138, 31))
        self.lblFloodValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblFloodValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblFloodValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFloodValue.setObjectName(_fromUtf8("lblFloodValue"))
        self.lblFloodValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblIceValue = QtGui.QLabel(self.groupBox3)
        self.lblIceValue.setGeometry(QtCore.QRect(296, 157, 138, 31))
        self.lblIceValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblIceValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIceValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIceValue.setObjectName(_fromUtf8("lblIceValue"))
        self.lblIceValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblDroughtValue = QtGui.QLabel(self.groupBox3)
        self.lblDroughtValue.setGeometry(QtCore.QRect(296, 190, 138, 31))
        self.lblDroughtValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblDroughtValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDroughtValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDroughtValue.setObjectName(_fromUtf8("lblDroughtValue"))
        self.lblDroughtValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblTunderValue = QtGui.QLabel(self.groupBox3)
        self.lblTunderValue.setGeometry(QtCore.QRect(296, 223, 138, 31))
        self.lblTunderValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblTunderValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTunderValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTunderValue.setObjectName(_fromUtf8("lblTunderValue"))
        self.lblTunderValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())


        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))



        self.groupBox11 = QtGui.QGroupBox(self.tab_2)
        self.groupBox11.setGeometry(QtCore.QRect(233, 0, 471, 411))
        self.groupBox11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox11.setObjectName(_fromUtf8("groupBox11"))
        self.groupBox11.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.gridLayout1 = QtGui.QGridLayout(self.groupBox11)
        self.gridLayout1.setObjectName(_fromUtf8("gridLayout1"))
        self.lblHazards1 = QtGui.QLabel(self.groupBox11)
        self.lblHazards1.setFrameShape(QtGui.QFrame.Box)
        self.lblHazards1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblHazards1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHazards1.setObjectName(_fromUtf8("lblHazards1"))
        self.lblHazards1.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout1.addWidget(self.lblHazards1, 0, 0, 7, 1)
        self.lblRain1 = QtGui.QCheckBox(self.groupBox11)
        self.lblRain1.setEnabled(True)
        self.lblRain1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblRain1.setChecked(True)
        self.lblRain1.setObjectName(_fromUtf8("lblRain1"))
        self.lblRain1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblRain1, 0, 1, 1, 1)
        self.lblRainValue1 = QtGui.QLabel(self.groupBox11)
        self.lblRainValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblRainValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblRainValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRainValue1.setObjectName(_fromUtf8("lblRainValue1"))
        self.lblRainValue1.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblRainValue1, 0, 2, 1, 1)
        self.cmbRain1 = QtGui.QComboBox(self.groupBox11)
        self.cmbRain1.setObjectName(_fromUtf8("cmbRain1"))
        self.cmbRain1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.cmbRain1, 0, 3, 1, 1)

        self.lblEarthquake1 = QtGui.QCheckBox(self.groupBox11)
        self.lblEarthquake1.setEnabled(True)
        self.lblEarthquake1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblEarthquake1.setChecked(True)
        self.lblEarthquake1.setObjectName(_fromUtf8("lblEarthquake1"))
        self.lblEarthquake1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblEarthquake1, 1, 1, 1, 1)
        self.lblEarthquakeValue1 = QtGui.QLabel(self.groupBox11)
        self.lblEarthquakeValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblEarthquakeValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblEarthquakeValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEarthquakeValue1.setObjectName(_fromUtf8("lblEarthquakeValue1"))
        self.lblEarthquakeValue1.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblEarthquakeValue1, 1, 2, 1, 1)
        self.cmbEarthquak1 = QtGui.QComboBox(self.groupBox11)
        self.cmbEarthquak1.setObjectName(_fromUtf8("cmbEarthquak"))
        self.cmbEarthquak1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout1.addWidget(self.cmbEarthquak1, 1, 3, 1, 1)

        self.lblLandslide1 = QtGui.QCheckBox(self.groupBox11)
        self.lblLandslide1.setEnabled(True)
        self.lblLandslide1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblLandslide1.setChecked(True)
        self.lblLandslide1.setObjectName(_fromUtf8("lblLandslide1"))
        self.lblLandslide1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblLandslide1, 2, 1, 1, 1)
        self.lblLandslideValue1 = QtGui.QLabel(self.groupBox11)
        self.lblLandslideValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblLandslideValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblLandslideValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLandslideValue1.setObjectName(_fromUtf8("lblLandslideValue"))
        self.lblLandslideValue1.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblLandslideValue1, 2, 2, 1, 1)
        self.cmbLandslide1 = QtGui.QComboBox(self.groupBox11)
        self.cmbLandslide1.setObjectName(_fromUtf8("cmbLandslide1"))
        self.cmbLandslide1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout1.addWidget(self.cmbLandslide1, 2, 3, 1, 1)

        self.lblFlood1 = QtGui.QCheckBox(self.groupBox11)
        self.lblFlood1.setEnabled(True)
        self.lblFlood1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblFlood1.setChecked(True)
        self.lblFlood1.setObjectName(_fromUtf8("lblFlood1"))
        self.lblFlood1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblFlood1, 3, 1, 1, 1)
        self.lblFloodValue1 = QtGui.QLabel(self.groupBox11)
        self.lblFloodValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblFloodValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblFloodValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFloodValue1.setObjectName(_fromUtf8("lblFloodValue1"))
        self.lblFloodValue1.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblFloodValue1, 3, 2, 1, 1)
        self.cmbFlood1 = QtGui.QComboBox(self.groupBox11)
        self.cmbFlood1.setObjectName(_fromUtf8("cmbFlood"))
        self.cmbFlood1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout1.addWidget(self.cmbFlood1, 3, 3, 1, 1)

        self.lblIce1 = QtGui.QCheckBox(self.groupBox11)
        self.lblIce1.setEnabled(True)
        self.lblIce1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblIce1.setChecked(True)
        self.lblIce1.setObjectName(_fromUtf8("lblIce"))
        self.lblIce1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblIce1, 4, 1, 1, 1)
        self.lblIceValue1 = QtGui.QLabel(self.groupBox11)
        self.lblIceValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblIceValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIceValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIceValue1.setObjectName(_fromUtf8("lblIceValue"))
        self.lblIceValue1.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblIceValue1, 4, 2, 1, 1)
        self.cmbIce1 = QtGui.QComboBox(self.groupBox11)
        self.cmbIce1.setObjectName(_fromUtf8("cmbIce"))
        self.cmbIce1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout1.addWidget(self.cmbIce1, 4, 3, 1, 1)

        self.lblDrought1 = QtGui.QCheckBox(self.groupBox11)
        self.lblDrought1.setEnabled(True)
        self.lblDrought1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblDrought1.setChecked(True)
        self.lblDrought1.setObjectName(_fromUtf8("lblDrought"))
        self.lblDrought1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblDrought1, 5, 1, 1, 1)
        self.lblDroughtValue1 = QtGui.QLabel(self.groupBox11)
        self.lblDroughtValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblDroughtValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDroughtValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDroughtValue1.setObjectName(_fromUtf8("lblDroughtValue1"))
        self.lblDroughtValue1.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblDroughtValue1, 5, 2, 1, 1)
        self.cmbDrought1 = QtGui.QComboBox(self.groupBox11)
        self.cmbDrought1.setObjectName(_fromUtf8("cmbDrought1"))
        self.cmbDrought1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout1.addWidget(self.cmbDrought1, 5, 3, 1, 1)

        self.lblTunder1 = QtGui.QCheckBox(self.groupBox11)
        self.lblTunder1.setEnabled(True)
        self.lblTunder1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTunder1.setChecked(True)
        self.lblTunder1.setObjectName(_fromUtf8("lblTunder1"))
        self.lblTunder1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblTunder1, 6, 1, 1, 1)
        self.lblTunderValue1 = QtGui.QLabel(self.groupBox11)
        self.lblTunderValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblTunderValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTunderValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTunderValue1.setObjectName(_fromUtf8("lblTunderValue1"))
        self.lblTunderValue1.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblTunderValue1, 6, 2, 1, 1)
        self.cmbTunder1 = QtGui.QComboBox(self.groupBox11)
        self.cmbTunder1.setObjectName(_fromUtf8("cmbTunder"))
        self.cmbTunder1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout1.addWidget(self.cmbTunder1, 6, 3, 1, 1)
        self.lblAmenity1 = QtGui.QCheckBox(self.groupBox11)
        self.lblAmenity1.setEnabled(True)
        self.lblAmenity1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAmenity1.setChecked(False)
        self.lblAmenity1.setObjectName(_fromUtf8("lblAmenity"))
        self.lblAmenity1.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout1.addWidget(self.lblAmenity1, 7, 1, 1, 1)
        self.lblAmenityValue1 = QtGui.QComboBox(self.groupBox11)
        self.lblAmenityValue1.setObjectName(_fromUtf8("lblAmenityValue1"))
        self.lblAmenityValue1.setStyleSheet("QComboBox { background-color: %s }" % col5.name())

        self.gridLayout1.addWidget(self.lblAmenityValue1, 7, 2, 1, 1)
        self.cmbRain_81 = QtGui.QComboBox(self.groupBox11)
        self.cmbRain_81.setObjectName(_fromUtf8("cmbRain_81"))
        self.cmbRain_81.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout1.addWidget(self.cmbRain_81, 7, 3, 1, 1)
        self.lbl1 = QtGui.QLabel(self.tab_2)
        self.lbl1.setGeometry(QtCore.QRect(2, 10, 230, 601))
        self.lbl1.setObjectName(_fromUtf8("graphicsView"))
        pixmap11=QtGui.QPixmap("Icons/iczm_img1.png")
        self.lbl1.setScaledContents(True)
        self.lbl1.setPixmap(pixmap11)

        self.groupBox21 = QtGui.QGroupBox(self.tab_2)
        self.groupBox21.setGeometry(QtCore.QRect(233, 420, 471, 221))
        self.groupBox21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox21.setObjectName(_fromUtf8("groupBox21"))
        self.groupBox21.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.btnHazardCalculate1 = QtGui.QPushButton(self.groupBox21)
        self.btnHazardCalculate1.setGeometry(QtCore.QRect(10, 20, 221, 151))
        self.btnHazardCalculate1.setObjectName(_fromUtf8("btnHazardCalculate1"))
        self.btnHazardCalculate1.setStyleSheet("QPushButton { background-color: %s }" % col4.name())

        self.lblHazardValue1 = QtGui.QLabel(self.groupBox21)
        self.lblHazardValue1.setGeometry(QtCore.QRect(240, 56, 210, 81))
        self.lblHazardValue1.setStyleSheet("QLabel { background-color: %s }" % col3.name())

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblHazardValue1.setFont(font)
        self.lblHazardValue1.setFrameShape(QtGui.QFrame.Panel)
        self.lblHazardValue1.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblHazardValue1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHazardValue1.setObjectName(_fromUtf8("lblHazardValue1"))

        QtCore.QObject.connect(self.btnHazardCalculate1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hazardCalculate)


        txtNo=_translate("formHazardDialog", "بدون اهمیت", None)
        txtLow=_translate("formHazardDialog", "کم اهمیت", None)
        txtMeddium=_translate("formHazardDialog", "با اهمیت متوسط", None)
        txtHigh=_translate("formHazardDialog", "با اهمیت زیاد", None)

        self.cmbRain1.addItem(txtNo)
        self.cmbRain1.addItem(txtLow)
        self.cmbRain1.addItem(txtMeddium)
        self.cmbRain1.addItem(txtHigh)

        self.cmbEarthquak1.addItem(txtNo)
        self.cmbEarthquak1.addItem(txtLow)
        self.cmbEarthquak1.addItem(txtMeddium)
        self.cmbEarthquak1.addItem(txtHigh)

        self.cmbLandslide1.addItem(txtNo)
        self.cmbLandslide1.addItem(txtLow)
        self.cmbLandslide1.addItem(txtMeddium)
        self.cmbLandslide1.addItem(txtHigh)


        self.cmbFlood1.addItem(txtNo)
        self.cmbFlood1.addItem(txtLow)
        self.cmbFlood1.addItem(txtMeddium)
        self.cmbFlood1.addItem(txtHigh)

        self.cmbIce1.addItem(txtNo)
        self.cmbIce1.addItem(txtLow)
        self.cmbIce1.addItem(txtMeddium)
        self.cmbIce1.addItem(txtHigh)

        self.cmbDrought1.addItem(txtNo)
        self.cmbDrought1.addItem(txtLow)
        self.cmbDrought1.addItem(txtMeddium)
        self.cmbDrought1.addItem(txtHigh)


        self.cmbTunder1.addItem(txtNo)
        self.cmbTunder1.addItem(txtLow)
        self.cmbTunder1.addItem(txtMeddium)
        self.cmbTunder1.addItem(txtHigh)

        self.cmbRain_81.addItem(txtNo)
        self.cmbRain_81.addItem(txtLow)
        self.cmbRain_81.addItem(txtMeddium)
        self.cmbRain_81.addItem(txtHigh)

        self.lblAmenityValue1.addItem(_translate("formHazardDialog", "فاقد خطر", None))
        self.lblAmenityValue1.addItem(_translate("formHazardDialog", "خطرکم", None))
        self.lblAmenityValue1.addItem(_translate("formHazardDialog", "خطر متوسط", None))
        self.lblAmenityValue1.addItem(_translate("formHazardDialog", "خطر زیاد", None))



        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))

        self.groupBox12 = QtGui.QGroupBox(self.tab_3)
        self.groupBox12.setGeometry(QtCore.QRect(348, 0, 345, 330))
        self.groupBox12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox12.setObjectName(_fromUtf8("groupBox12"))
        self.groupBox12.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())
        self.gridLayout2 = QtGui.QGridLayout(self.groupBox12)
        self.gridLayout2.setObjectName(_fromUtf8("gridLayout2"))
        self.lblIndustValue2 = QtGui.QLabel(self.groupBox12)
        self.lblIndustValue2.setFrameShape(QtGui.QFrame.Panel)
        self.lblIndustValue2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndustValue2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndustValue2.setObjectName(_fromUtf8("lblIndustValue"))
        self.lblIndustValue2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout2.addWidget(self.lblIndustValue2, 2, 1, 1, 1)
        self.lblTourismValue2 = QtGui.QLabel(self.groupBox12)
        self.lblTourismValue2.setFrameShape(QtGui.QFrame.Panel)
        self.lblTourismValue2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourismValue2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourismValue2.setObjectName(_fromUtf8("lblTourismValue"))
        self.lblTourismValue2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout2.addWidget(self.lblTourismValue2, 1, 1, 1, 1)
        self.lblIndust2 = QtGui.QLabel(self.groupBox12)
        self.lblIndust2.setFrameShape(QtGui.QFrame.Box)
        self.lblIndust2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndust2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndust2.setObjectName(_fromUtf8("lblIndust"))
        self.lblIndust2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout2.addWidget(self.lblIndust2, 2, 0, 1, 1)
        self.lblResid2 = QtGui.QLabel(self.groupBox12)
        self.lblResid2.setFrameShape(QtGui.QFrame.Box)
        self.lblResid2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResid2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResid2.setObjectName(_fromUtf8("lblResid"))
        self.lblResid2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout2.addWidget(self.lblResid2, 3, 0, 1, 1)
        self.lblAgriValue2 = QtGui.QLabel(self.groupBox12)
        self.lblAgriValue2.setFrameShape(QtGui.QFrame.Panel)
        self.lblAgriValue2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgriValue2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgriValue2.setObjectName(_fromUtf8("lblAgriValue"))
        self.lblAgriValue2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout2.addWidget(self.lblAgriValue2, 0, 1, 1, 1)
        self.lblResidValue2 = QtGui.QLabel(self.groupBox12)
        self.lblResidValue2.setFrameShape(QtGui.QFrame.Panel)
        self.lblResidValue2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResidValue2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResidValue2.setObjectName(_fromUtf8("lblResidValue2"))
        self.lblResidValue2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout2.addWidget(self.lblResidValue2, 3, 1, 1, 1)
        self.lblTourism2 = QtGui.QLabel(self.groupBox12)
        self.lblTourism2.setFrameShape(QtGui.QFrame.Box)
        self.lblTourism2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourism2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourism2.setObjectName(_fromUtf8("lblTourism2"))
        self.lblTourism2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout2.addWidget(self.lblTourism2, 1, 0, 1, 1)
        self.lblAgri2 = QtGui.QLabel(self.groupBox12)
        self.lblAgri2.setFrameShape(QtGui.QFrame.Box)
        self.lblAgri2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgri2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgri2.setObjectName(_fromUtf8("lblAgri2"))
        self.lblAgri2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout2.addWidget(self.lblAgri2, 0, 0, 1, 1)
        self.groupBox1_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox1_2.setGeometry(QtCore.QRect(2, 0, 345, 330))
        self.groupBox1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox1_2.setObjectName(_fromUtf8("groupBox1_2"))
        self.groupBox1_2.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox1_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblTourism_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblTourism_2.setFrameShape(QtGui.QFrame.Box)
        self.lblTourism_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourism_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourism_2.setObjectName(_fromUtf8("lblTourism_2"))
        self.lblTourism_2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout_2.addWidget(self.lblTourism_2, 1, 0, 1, 1)
        self.lblIndust_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblIndust_2.setFrameShape(QtGui.QFrame.Box)
        self.lblIndust_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndust_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndust_2.setObjectName(_fromUtf8("lblIndust_2"))
        self.lblIndust_2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout_2.addWidget(self.lblIndust_2, 2, 0, 1, 1)
        self.lblTourismValue_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblTourismValue_2.setFrameShape(QtGui.QFrame.Panel)
        self.lblTourismValue_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourismValue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourismValue_2.setObjectName(_fromUtf8("lblTourismValue_2"))
        self.lblTourismValue_2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout_2.addWidget(self.lblTourismValue_2, 1, 1, 1, 1)
        self.lblResid_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblResid_2.setFrameShape(QtGui.QFrame.Box)
        self.lblResid_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResid_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResid_2.setObjectName(_fromUtf8("lblResid_2"))
        self.lblResid_2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout_2.addWidget(self.lblResid_2, 3, 0, 1, 1)
        self.lblResidValue_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblResidValue_2.setFrameShape(QtGui.QFrame.Panel)
        self.lblResidValue_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResidValue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResidValue_2.setObjectName(_fromUtf8("lblResidValue_2"))
        self.lblResidValue_2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout_2.addWidget(self.lblResidValue_2, 3, 1, 1, 1)
        self.lblAgri_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblAgri_2.setFrameShape(QtGui.QFrame.Box)
        self.lblAgri_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgri_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgri_2.setObjectName(_fromUtf8("lblAgri_2"))
        self.lblAgri_2.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout_2.addWidget(self.lblAgri_2, 0, 0, 1, 1)
        self.lblIndustValue_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblIndustValue_2.setFrameShape(QtGui.QFrame.Panel)
        self.lblIndustValue_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndustValue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndustValue_2.setObjectName(_fromUtf8("lblIndustValue_2"))
        self.lblIndustValue_2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout_2.addWidget(self.lblIndustValue_2, 2, 1, 1, 1)
        self.lblAgriValue_2 = QtGui.QLabel(self.groupBox1_2)
        self.lblAgriValue_2.setFrameShape(QtGui.QFrame.Panel)
        self.lblAgriValue_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgriValue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgriValue_2.setObjectName(_fromUtf8("lblAgriValue_2"))
        self.lblAgriValue_2.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout_2.addWidget(self.lblAgriValue_2, 0, 1, 1, 1)

        pixmap22=QtGui.QPixmap("Icons/Software_img3.png")
        self.lbl22 = QtGui.QLabel(self.tab_3)

        self.lbl22.setGeometry(QtCore.QRect(2, 340, 700, 290))
        self.lbl22.setObjectName(_fromUtf8("graphic2"))

        self.lbl22.setScaledContents(True)

        self.lbl22.setPixmap(pixmap22)


        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))

        self.groupBox13 = QtGui.QGroupBox(self.tab_4)
        self.groupBox13.setGeometry(QtCore.QRect(10, 10, 490, 431))
        self.groupBox13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox13.setObjectName(_fromUtf8("groupBox13"))

        self.groupBox13.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.gridLayout3 = QtGui.QGridLayout(self.groupBox13)
        self.gridLayout3.setObjectName(_fromUtf8("gridLayout3"))
        self.lblResidential3 = QtGui.QLabel(self.groupBox13)
        self.lblResidential3.setFrameShape(QtGui.QFrame.Box)
        self.lblResidential3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResidential3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResidential3.setObjectName(_fromUtf8("lblResidential3"))

        self.lblResidential3.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout3.addWidget(self.lblResidential3, 4, 0, 1, 1)
        self.lblIndust3 = QtGui.QLabel(self.groupBox13)
        self.lblIndust3.setFrameShape(QtGui.QFrame.Box)
        self.lblIndust3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndust3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndust3.setObjectName(_fromUtf8("lblIndust3"))
        self.lblIndust3.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout3.addWidget(self.lblIndust3, 2, 0, 1, 1)
        self.lblConservValue3 = QtGui.QLabel(self.groupBox13)
        self.lblConservValue3.setFrameShape(QtGui.QFrame.Panel)
        self.lblConservValue3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblConservValue3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConservValue3.setObjectName(_fromUtf8("lblConservValue"))
        self.lblConservValue3.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout3.addWidget(self.lblConservValue3, 3, 1, 1, 1)
        self.lblConsetv3 = QtGui.QLabel(self.groupBox13)
        self.lblConsetv3.setFrameShape(QtGui.QFrame.Box)
        self.lblConsetv3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblConsetv3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConsetv3.setObjectName(_fromUtf8("lblConsetv3"))
        self.lblConsetv3.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout3.addWidget(self.lblConsetv3, 3, 0, 1, 1)
        self.lblTourismValue3 = QtGui.QLabel(self.groupBox13)
        self.lblTourismValue3.setFrameShape(QtGui.QFrame.Panel)
        self.lblTourismValue3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourismValue3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourismValue3.setObjectName(_fromUtf8("lblTourismValue3"))
        self.lblTourismValue3.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout3.addWidget(self.lblTourismValue3, 1, 1, 1, 1)
        self.lblAgriValue3 = QtGui.QLabel(self.groupBox13)
        self.lblAgriValue3.setFrameShape(QtGui.QFrame.Panel)
        self.lblAgriValue3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgriValue3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgriValue3.setObjectName(_fromUtf8("lblAgriValue3"))
        self.lblAgriValue3.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout3.addWidget(self.lblAgriValue3, 0, 1, 1, 1)
        self.lblIndustValue3 = QtGui.QLabel(self.groupBox13)
        self.lblIndustValue3.setFrameShape(QtGui.QFrame.Panel)
        self.lblIndustValue3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndustValue3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndustValue3.setObjectName(_fromUtf8("lblIndustValue3"))
        self.lblIndustValue3.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout3.addWidget(self.lblIndustValue3, 2, 1, 1, 1)
        self.lblAgri3 = QtGui.QLabel(self.groupBox13)
        self.lblAgri3.setFrameShape(QtGui.QFrame.Box)
        self.lblAgri3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgri3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgri3.setObjectName(_fromUtf8("lblAgri3"))
        self.lblAgri3.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout3.addWidget(self.lblAgri3, 0, 0, 1, 1)
        self.lblResidentialValue3 = QtGui.QLabel(self.groupBox13)
        self.lblResidentialValue3.setFrameShape(QtGui.QFrame.Panel)
        self.lblResidentialValue3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResidentialValue3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResidentialValue3.setObjectName(_fromUtf8("lblResidentialValue3"))
        self.lblResidentialValue3.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout3.addWidget(self.lblResidentialValue3, 4, 1, 1, 1)
        self.lblTourism3 = QtGui.QLabel(self.groupBox13)
        self.lblTourism3.setFrameShape(QtGui.QFrame.Box)
        self.lblTourism3.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourism3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourism3.setObjectName(_fromUtf8("lblTourism3"))
        self.lblTourism3.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout3.addWidget(self.lblTourism3, 1, 0, 1, 1)
        #pixmap1=QtGui.QPixmap("Icons/iczm_img1.png")
        pixmap13=QtGui.QPixmap("Icons/Software_img2.png")
        pixmap23=QtGui.QPixmap("Icons/iczm_img2.png")
        self.lbl13 = QtGui.QLabel(self.tab_4)
        self.lbl13.setGeometry(QtCore.QRect(501, 5, 190, 441))
        self.lbl13.setObjectName(_fromUtf8("graphic1"))
        self.lbl13.setScaledContents(True)
        self.lbl13.setPixmap(pixmap13)
        self.lbl23 = QtGui.QLabel(self.tab_4)
        self.lbl23.setGeometry(QtCore.QRect(10, 445, 685, 241))
        self.lbl23.setObjectName(_fromUtf8("graphic2"))
        self.lbl23.setScaledContents(True)
        self.lbl23.setPixmap(pixmap23)



        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.bottonLaws, QtCore.SIGNAL(_fromUtf8("clicked()")), self.setLaws)
        self.setValues()
        self.setValues11()
        self.setValues3()
        self.setValues4()


    def extractData(self,where):
        if where == 0:
            self.Result = self.readSpatialData(self.North_Files,self.North_SpecialFiles,self.x,self.y)

            if str(self.Result[("Zoning_North","Code")]) <> '0':
                self.Extracted=True
            else:
                self.Extracted=False
        else:
            self.Result = self.readSpatialData(self.South_Files,self.South_SpecialFiles,self.x,self.y)
            if str(self.Result[("Zoning_South","Code")]) <> '0':
                self.Extracted=True
            else:
                self.Extracted=False

    def readSpatialData(self,filenames,specialfiles,x,y):
        out={}
        driver = ogr.GetDriverByName('ESRI Shapefile')
        p=ogr.Geometry(ogr.wkbPoint)
        p.AddPoint(x,y)
        for f in filenames:
            ds = driver.Open(self.path+"/Data/"+self.selectedProvince+"/"+f+'.shp',0)
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
                fsp = open(self.path+"/Data/"+self.selectedProvince+"/"+f+".txt", 'r')
                mtx = [line.rstrip().split(',') for line in fsp.readlines()]
                fsp.close()
                v=[line[0] for line in mtx[1:]]
                oID = v.index(str(out[(f,'Code')]))
                oID+=1
                for fld in self.FieldNames[f][:-1]:
                    fID=mtx[0].index(fld)
                    out[(f,fld)]=mtx[oID][fID]
        return out


    def retranslateUi(self):
        self.setWindowTitle(_translate("ICZMDSS_ArcGIS", "سامانه پشتیبان تصمیم گیری برای مدیریت یکپارچه مناطق ساحلی", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ICZMDSS_ArcGIS", "نمایش پهنه و ضابطه", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ICZMDSS_ArcGIS", "مخاطرات", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ICZMDSS_ArcGIS", "فرصت ها و تهدید های دریایی", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("ICZMDSS_ArcGIS", "توان اکولوژیک", None))
        self.groupBox1.setToolTip(_translate("funcZoneDialog", "پهنه عملکردی", None))
        self.groupBox1.setStatusTip(_translate("funcZoneDialog", "پهنه عملکردی", None))
        self.groupBox1.setTitle(_translate("funcZoneDialog", "پهنه عملکردی", None))
        self.lblZoneCode.setText(_translate("funcZoneDialog", "کد پهنه", None))
        self.lblZoneName.setText(_translate("funcZoneDialog", "نام پهنه", None))
        self.lblLaws.setText(_translate("funcZoneDialog", "ضوابط", None))
        self.lblZoneCodeValue.setText(_translate("funcZoneDialog", "Code", None))
        self.lblZoneNameValue.setText(_translate("funcZoneDialog", "نام پهنه", None))
        self.bottonLaws.setText(_translate("funcZoneDialog", "قوانین", None))
        self.groupBox2.setToolTip(_translate("funcZoneDialog", "مرز مدیریتی", None))
        self.groupBox2.setStatusTip(_translate("funcZoneDialog", "مرز مدیریتی", None))
        self.groupBox2.setTitle(_translate("funcZoneDialog", "مرز مدیریتی", None))
        self.lblDetails.setText(_translate("funcZoneDialog", "توضیحات", None))
        self.lblManageLaws.setText(_translate("funcZoneDialog", "ضوابط", None))
        self.lblDetailsValue.setText(_translate("funcZoneDialog", "توضیحات", None))
        self.lblManageLawsValue.setText(_translate("funcZoneDialog", "ضوابط مدیریتی", None))
        self.groupBox3.setTitle(_translate("funcZoneDialog", "مخاطرات", None))
        self.lblHazards.setText(_translate("funcZoneDialog", "مخاطرات", None))
        self.lblRain.setText(_translate("funcZoneDialog", "باران", None))
        self.lblEarthquake.setText(_translate("funcZoneDialog", "زلزله", None))
        self.lblLandslide.setText(_translate("funcZoneDialog", "رانش", None))
        self.lblFlood.setText(_translate("funcZoneDialog", "سیل", None))
        self.lblIce.setText(_translate("funcZoneDialog", "یخ بندان", None))
        self.lblDrought.setText(_translate("funcZoneDialog", "خشکسالی", None))
        self.lblTunder.setText(_translate("funcZoneDialog", "طوفان", None))
        self.lblRainValue.setText(_translate("funcZoneDialog", "-", None))
        self.lblEarthquakeValue.setText(_translate("funcZoneDialog", "-", None))
        self.lblLandslideValue.setText(_translate("funcZoneDialog", "-", None))
        self.lblFloodValue.setText(_translate("funcZoneDialog", "-", None))
        self.lblIceValue.setText(_translate("funcZoneDialog", "-", None))
        self.lblDroughtValue.setText(_translate("funcZoneDialog", "-", None))
        self.lblTunderValue.setText(_translate("funcZoneDialog", "-", None))


        self.groupBox11.setTitle(_translate("formHazardDialog", "مخاطرات", None))
        self.lblHazards1.setText(_translate("formHazardDialog", "مخاطرات", None))
        self.lblRain1.setText(_translate("formHazardDialog", "باران", None))
        self.lblRainValue1.setText(_translate("formHazardDialog", "-", None))
        self.lblEarthquake1.setText(_translate("formHazardDialog", "زلزله", None))
        self.lblEarthquakeValue1.setText(_translate("formHazardDialog", "-", None))
        self.lblLandslide1.setText(_translate("formHazardDialog", "رانش", None))
        self.lblLandslideValue1.setText(_translate("formHazardDialog", "-", None))
        self.lblFlood1.setText(_translate("formHazardDialog", "سیل", None))
        self.lblFloodValue1.setText(_translate("formHazardDialog", "-", None))
        self.lblIce1.setText(_translate("formHazardDialog", "یخبندان", None))
        self.lblIceValue1.setText(_translate("formHazardDialog", "-", None))
        self.lblDrought1.setText(_translate("formHazardDialog", "خشکسالی", None))
        self.lblDroughtValue1.setText(_translate("formHazardDialog", "-", None))
        self.lblTunder1.setText(_translate("formHazardDialog", "طوفان", None))
        self.lblTunderValue1.setText(_translate("formHazardDialog", "-", None))
        self.lblAmenity1.setText(_translate("formHazardDialog", "امنیتی", None))
        self.groupBox21.setTitle(_translate("formHazardDialog", "محاسبه برآیند مخاطرات", None))
        self.btnHazardCalculate1.setText(_translate("formHazardDialog", "برآیند مخاطرات", None))
        self.lblHazardValue1.setText(_translate("formHazardDialog", "0", None))

        self.groupBox12.setTitle(_translate("frmOptThreatDialog", "تهدیدهای دریایی", None))
        self.lblIndustValue2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblTourismValue2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblIndust2.setText(_translate("frmOptThreatDialog", "صنعتی", None))
        self.lblResid2.setText(_translate("frmOptThreatDialog", "سکونت", None))
        self.lblAgriValue2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblResidValue2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblTourism2.setText(_translate("frmOptThreatDialog", "گردشگری", None))
        self.lblAgri2.setText(_translate("frmOptThreatDialog", "کشاورزی", None))
        self.groupBox1_2.setTitle(_translate("frmOptThreatDialog", "فرصتهای دریایی", None))
        self.lblTourism_2.setText(_translate("frmOptThreatDialog", "گردشگری", None))
        self.lblIndust_2.setText(_translate("frmOptThreatDialog", "صنعتی", None))
        self.lblTourismValue_2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblResid_2.setText(_translate("frmOptThreatDialog", "سکونت", None))
        self.lblResidValue_2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblAgri_2.setText(_translate("frmOptThreatDialog", "کشاورزی", None))
        self.lblIndustValue_2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblAgriValue_2.setText(_translate("frmOptThreatDialog", "-", None))

        self.groupBox13.setTitle(_translate("formEcologicDialog", "توان اکولوژیک", None))
        self.lblResidential3.setText(_translate("formEcologicDialog", "شهری", None))
        self.lblIndust3.setText(_translate("formEcologicDialog", "صنعتی", None))
        self.lblConservValue3.setText(_translate("formEcologicDialog", "-", None))
        self.lblConsetv3.setText(_translate("formEcologicDialog", "حفاظتی", None))
        self.lblTourismValue3.setText(_translate("formEcologicDialog", "-", None))
        self.lblAgriValue3.setText(_translate("formEcologicDialog", "-", None))
        self.lblIndustValue3.setText(_translate("formEcologicDialog", "-", None))
        self.lblAgri3.setText(_translate("formEcologicDialog", "کشاورزی", None))
        self.lblResidentialValue3.setText(_translate("formEcologicDialog", "-", None))
        self.lblTourism3.setText(_translate("formEcologicDialog", "گردشگری", None))


    def setLaws(self):
        self.focusAct=False
        self.formTextBrowser=formTextBrowser(self)
        self.formTextBrowser.show()
        if self.where == 0:
            self.formTextBrowser.textBrowser.setText(_translate("formTextBrowser",str(self.Result[("Zoning_North","Regulation")]),None))
        else:
            self.formTextBrowser.textBrowser.setText(_translate("formTextBrowser",str(self.Result[("Zoning_South","Regulation")]),None))

    def hazardCalculate(self):
        if self.where == 0:
            objList=[self.lblRain1,self.lblEarthquake1,self.lblLandslide1,self.lblFlood1,self.lblIce1,self.lblDrought1,self.lblTunder1]
            objListWeight=[self.cmbRain1,self.cmbEarthquak1,self.cmbLandslide1,self.cmbFlood1,self.cmbIce1,self.cmbDrought1,self.cmbTunder1]
            resList = [("Hazards_North","R"),("Hazards_North","Q"),("Hazards_North","L"),("Hazards_North","F"),("Hazards_North","I"),("Hazards_North","K"),("Hazards_North","S")]
        else:
            objList=[self.lblRain1,self.lblEarthquake1,self.lblLandslide1,self.lblDrought1,self.lblTunder1]
            objListWeight=[self.cmbRain1,self.cmbEarthquak1,self.cmbLandslide1,self.cmbDrought1,self.cmbTunder1]
            resList = [("Hazards_South","R"),("Hazards_South","Q"),("Hazards_South","L"),("Hazards_South","K"),("Hazards_South","S")]


        vals=[]
        weights=[]
        for i in range(len(objList)):
            if objList[i].checkState() == QtCore.Qt.Checked:
                try:
                    vals.append(self.Result[resList[i]])
                    weights.append(objListWeight[i].currentIndex())
                except:
                    pass
        if self.lblAmenity1.checkState() == QtCore.Qt.Checked:
                vals.append(self.lblAmenityValue1.currentIndex())
                weights.append(self.cmbRain_81.currentIndex())
        totalHazard=0
        for i in range(len(vals)):
            totalHazard+=vals[i]*weights[i]
        totalHazard=round(totalHazard/(len(weights)*9.0) * 100,2)
        self.lblHazardValue1.setText(str(totalHazard)+' %')


    def extResult(self,objList,resList):
        for i in range(len(objList)):
            try:
                val=self.Result[resList[i]]
            except:
                val=9

            if val == 0:
                objList[i].setText(_translate("funcZoneDialog", "فاقد خطر", None))
            elif val == 1:
                objList[i].setText(_translate("funcZoneDialog", "خطرکم", None))
            elif val == 2:
                objList[i].setText(_translate("funcZoneDialog", "خطر متوسط", None))
            elif val == 3:
                objList[i].setText(_translate("funcZoneDialog", "خطر زیاد", None))
            else:
                objList[i].setText("-")



    def setValues11(self):
        if self.where == 0:
            self.extResult([self.lblRainValue1,self.lblEarthquakeValue1,self.lblLandslideValue1,self.lblFloodValue1,self.lblIceValue1,self.lblDroughtValue1,self.lblTunderValue1],[("Hazards_North","R"),("Hazards_North","Q"),("Hazards_North","L"),("Hazards_North","F"),("Hazards_North","I"),("Hazards_North","K"),("Hazards_North","S")])
        else:
            self.extResult([self.lblRainValue1,self.lblEarthquakeValue1,self.lblLandslideValue1,self.lblDroughtValue1,self.lblTunderValue1],[("Hazards_South","R"),("Hazards_South","Q"),("Hazards_South","L"),("Hazards_South","K"),("Hazards_South","S")])


    def setValues(self):
        self.setValues2()
        if self.where == 0:
            self.extResult([self.lblRainValue,self.lblEarthquakeValue,self.lblLandslideValue,self.lblFloodValue,self.lblIceValue,self.lblDroughtValue,self.lblTunderValue],[("Hazards_North","R"),("Hazards_North","Q"),("Hazards_North","L"),("Hazards_North","F"),("Hazards_North","I"),("Hazards_North","K"),("Hazards_North","S")])
        else:
            self.extResult([self.lblRainValue,self.lblEarthquakeValue,self.lblLandslideValue,self.lblDroughtValue,self.lblTunderValue],[("Hazards_South","R"),("Hazards_South","Q"),("Hazards_South","L"),("Hazards_South","K"),("Hazards_South","S")])


    def setValues2(self):

        if self.where == 0:
            self.lblZoneCodeValue.setText(_translate("funcZoneDialog", str(self.Result[("Zoning_North","Result")]), None))
            self.lblZoneNameValue.setText(_translate("funcZoneDialog", str(self.Result[("Zoning_North","Name")]), None))
            self.lblDetailsValue.setText(_translate("funcZoneDialog", str(self.Result[("ManageB_North","name")]), None))
            self.lblManageLawsValue.setText(_translate("funcZoneDialog",  str(self.Result[("ManageB_North","MC")]), None))

        elif self.where == 1:
            self.lblZoneCodeValue.setText(_translate("funcZoneDialog", str(self.Result[("Zoning_South","Result")]), None))
            self.lblZoneNameValue.setText(_translate("funcZoneDialog", str(self.Result[("Zoning_South","Name")]), None))
            self.lblDetailsValue.setText(_translate("funcZoneDialog", str(self.Result[("ManageB_South","Name")]), None))
            self.lblManageLawsValue.setText(_translate("funcZoneDialog",  str(str(self.Result[("ManageB_South","MC")])), None))

##    def focusOutEvent(self, event):
##        if (self.focusAct):
##            self.close()
##        else:
##            pass



    def extResult2(self,objList,resList):
        for i in range(len(objList)):
            try:
                val=self.Result[resList[i]]
            except:
                val=9

            if val == 0:
                objList[i].setText(_translate("frmOptThreatDialog", "بی اثر", None))
            elif val == 1:
                objList[i].setText(_translate("frmOptThreatDialog", "کم", None))
            elif val == 2:
                objList[i].setText(_translate("frmOptThreatDialog", "متوسط", None))
            elif val == 3:
                objList[i].setText(_translate("frmOptThreatDialog", "زیاد", None))
            else:
                objList[i].setText('-')

    def setValues3(self):
        if self.where == 0:
            self.extResult2([self.lblResidValue2,self.lblTourismValue2,self.lblAgriValue2,self.lblIndustValue2,self.lblResidValue_2,self.lblTourismValue_2,self.lblAgriValue_2,self.lblIndustValue_2],\
            [("Opportunity_North","O_Resid"),("Opportunity_North","O_Tour"),("Opportunity_North","O_Agri"),("Opportunity_North","O_Indust"),("Threat_North","T_Resid"),("Threat_North","T_Tour"),("Threat_North","T_Agri"),("Threat_North","T_Indust")])
        else:
            self.extResult2([self.lblResidValue2,self.lblTourismValue2,self.lblAgriValue2,self.lblIndustValue2,self.lblResidValue_2,self.lblTourismValue_2,self.lblAgriValue_2,self.lblIndustValue_2],\
            [("Opportunity_South","O_Resid"),("Opportunity_South","O_Tour"),("Opportunity_South","O_Agri"),("Opportunity_South","O_Indust"),("Threat_South","T_Resid"),("Threat_South","T_Tour"),("Threat_South","T_Agri"),("Threat_South","T_Indust")])

    def setValues4(self):

        if self.where == 0:
            self.lblConservValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_North","P_Conserv")]), None))
            self.lblTourismValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_North","P_Tour")]), None))
            self.lblAgriValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_North","P_Agri")]), None))
            self.lblIndustValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_North","P_Indust")]), None))
            self.lblResidentialValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_North","P_Urban")]), None))
        elif self.where == 1:
            self.lblConservValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_South","P_Conserv")]), None))
            self.lblTourismValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_South","P_Tour")]), None))
            self.lblAgriValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_South","P_Agri")]), None))
            self.lblIndustValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_South","P_Indust")]), None))
            self.lblResidentialValue3.setText(_translate("formEcologicDialog", str(self.Result[("Tavan_South","P_Urban")]), None))
def main():
    app = QtGui.QApplication(sys.argv)
    ui=arcgisDialog(sys.argv[1],int(sys.argv[2]),sys.argv[3],float(sys.argv[4]),float(sys.argv[5]))
    #ui=arcgisDialog("D:/ICZM_DSS",int("0"),"_Gilan",398981.4,4139379.2)
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


