# -*- coding: utf-8 -*-

# ICZM DSS
# Developed By Babak Naimi (SAP Consulting Engineers Co.)
# Client: PMO
# -- Dialog widget for functional zoning module

from PyQt4 import QtCore, QtGui
from formTextBrowser import *
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

class funcZoneDialog(QtGui.QDialog):
    def __init__(self, where,parent=None):
        super(funcZoneDialog,self).__init__(parent)
        self.setObjectName(_fromUtf8("funcZoneDialog"))
        self.resize(666, 651)

        col1 = QtGui.QColor(207, 209, 154)
        col2 = QtGui.QColor(236, 238, 176)
        col3 = QtGui.QColor(213, 255, 215)
        col4 = QtGui.QColor(230, 217, 255)
        col5 = QtGui.QColor(255, 245, 231)
        col6 = QtGui.QColor(254, 251, 136)
        self.setStyleSheet("QDialog { background-color: %s }" % col1.name())

        self.where=where
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        self.setFont(font)
        self.setModal(False)
        pixmap=QtGui.QPixmap("Icons/iczm_img1.png")
        self.lbl = QtGui.QLabel(self)
        self.lbl.setGeometry(QtCore.QRect(10, 10, 231, 571))
        self.lbl.setObjectName(_fromUtf8("graphicsView"))
        self.lbl.setScaledContents(True)
        self.lbl.setPixmap(pixmap)
        self.groupBox1 = QtGui.QGroupBox(self)
        self.groupBox1.setGeometry(QtCore.QRect(250, 3, 411, 121))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.groupBox1.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.widget = QtGui.QWidget(self.groupBox1)
        self.widget.setGeometry(QtCore.QRect(12, 22, 391, 91))
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
        self.groupBox2 = QtGui.QGroupBox(self)
        self.groupBox2.setGeometry(QtCore.QRect(250, 121, 411, 261))
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.groupBox2.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.widget1 = QtGui.QWidget(self.groupBox2)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 391, 20))
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
        self.widget2.setGeometry(QtCore.QRect(10, 50, 391, 201))
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
        self.groupBox3 = QtGui.QGroupBox(self)
        self.groupBox3.setGeometry(QtCore.QRect(250, 376, 411, 301))
        self.groupBox3.setObjectName(_fromUtf8("groupBox3"))
        self.groupBox3.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.lblHazards = QtGui.QLabel(self.groupBox3)
        self.lblHazards.setGeometry(QtCore.QRect(6, 23, 131, 225))
        self.lblHazards.setFrameShape(QtGui.QFrame.Panel)
        self.lblHazards.setFrameShadow(QtGui.QFrame.Raised)
        self.lblHazards.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHazards.setObjectName(_fromUtf8("lblHazards"))
        self.lblHazards.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblRain = QtGui.QLabel(self.groupBox3)
        self.lblRain.setGeometry(QtCore.QRect(140, 20, 121, 31))
        self.lblRain.setFrameShape(QtGui.QFrame.Box)
        self.lblRain.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblRain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRain.setObjectName(_fromUtf8("lblRain"))
        self.lblRain.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblEarthquake = QtGui.QLabel(self.groupBox3)
        self.lblEarthquake.setGeometry(QtCore.QRect(140, 53, 121, 31))
        self.lblEarthquake.setFrameShape(QtGui.QFrame.Box)
        self.lblEarthquake.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblEarthquake.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEarthquake.setObjectName(_fromUtf8("lblEarthquake"))
        self.lblEarthquake.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblLandslide = QtGui.QLabel(self.groupBox3)
        self.lblLandslide.setGeometry(QtCore.QRect(140, 86, 121, 31))
        self.lblLandslide.setFrameShape(QtGui.QFrame.Box)
        self.lblLandslide.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblLandslide.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLandslide.setObjectName(_fromUtf8("lblLandslide"))
        self.lblLandslide.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblFlood = QtGui.QLabel(self.groupBox3)
        self.lblFlood.setGeometry(QtCore.QRect(140, 123, 121, 31))
        self.lblFlood.setFrameShape(QtGui.QFrame.Box)
        self.lblFlood.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblFlood.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFlood.setObjectName(_fromUtf8("lblFlood"))
        self.lblFlood.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblIce = QtGui.QLabel(self.groupBox3)
        self.lblIce.setGeometry(QtCore.QRect(140, 157, 121, 31))
        self.lblIce.setFrameShape(QtGui.QFrame.Box)
        self.lblIce.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIce.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIce.setObjectName(_fromUtf8("lblIce"))
        self.lblIce.setStyleSheet("QLabel { background-color: %s }" % col4.name())


        self.lblDrought = QtGui.QLabel(self.groupBox3)
        self.lblDrought.setGeometry(QtCore.QRect(140, 190, 121, 31))
        self.lblDrought.setFrameShape(QtGui.QFrame.Box)
        self.lblDrought.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDrought.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDrought.setObjectName(_fromUtf8("lblDrought"))
        self.lblDrought.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.lblTunder = QtGui.QLabel(self.groupBox3)
        self.lblTunder.setGeometry(QtCore.QRect(140, 223, 121, 31))
        self.lblTunder.setFrameShape(QtGui.QFrame.Box)
        self.lblTunder.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTunder.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTunder.setObjectName(_fromUtf8("lblTunder"))
        self.lblTunder.setStyleSheet("QLabel { background-color: %s }" % col4.name())


        self.lblRainValue = QtGui.QLabel(self.groupBox3)
        self.lblRainValue.setGeometry(QtCore.QRect(264, 20, 141, 31))
        self.lblRainValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblRainValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblRainValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRainValue.setObjectName(_fromUtf8("lblRainValue"))
        self.lblRainValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblEarthquakeValue = QtGui.QLabel(self.groupBox3)
        self.lblEarthquakeValue.setGeometry(QtCore.QRect(264, 53, 141, 31))
        self.lblEarthquakeValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblEarthquakeValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblEarthquakeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEarthquakeValue.setObjectName(_fromUtf8("lblEarthquakeValue"))
        self.lblEarthquakeValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblLandslideValue = QtGui.QLabel(self.groupBox3)
        self.lblLandslideValue.setGeometry(QtCore.QRect(264, 86, 141, 31))
        self.lblLandslideValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblLandslideValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblLandslideValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLandslideValue.setObjectName(_fromUtf8("lblLandslideValue"))
        self.lblLandslideValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblFloodValue = QtGui.QLabel(self.groupBox3)
        self.lblFloodValue.setGeometry(QtCore.QRect(265, 123, 141, 31))
        self.lblFloodValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblFloodValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblFloodValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFloodValue.setObjectName(_fromUtf8("lblFloodValue"))
        self.lblFloodValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblIceValue = QtGui.QLabel(self.groupBox3)
        self.lblIceValue.setGeometry(QtCore.QRect(264, 157, 141, 31))
        self.lblIceValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblIceValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIceValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIceValue.setObjectName(_fromUtf8("lblIceValue"))
        self.lblIceValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblDroughtValue = QtGui.QLabel(self.groupBox3)
        self.lblDroughtValue.setGeometry(QtCore.QRect(265, 190, 141, 31))
        self.lblDroughtValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblDroughtValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDroughtValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDroughtValue.setObjectName(_fromUtf8("lblDroughtValue"))
        self.lblDroughtValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.lblTunderValue = QtGui.QLabel(self.groupBox3)
        self.lblTunderValue.setGeometry(QtCore.QRect(264, 223, 141, 31))
        self.lblTunderValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblTunderValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTunderValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTunderValue.setObjectName(_fromUtf8("lblTunderValue"))
        self.lblTunderValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.retranslateUi()
        self.setValues()
        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.bottonLaws, QtCore.SIGNAL(_fromUtf8("clicked()")), self.setLaws)
    def setLaws(self):
        self.formTextBrowser=formTextBrowser(self)
        self.formTextBrowser.show()
        if self.where == 0:
            self.formTextBrowser.textBrowser.setText(_translate("formTextBrowser",str(self.parent().Result[("Zoning_North","Regulation")]),None))
        else:
            self.formTextBrowser.textBrowser.setText(_translate("formTextBrowser",str(self.parent().Result[("Zoning_South","Regulation")]),None))
    def closeEvent(self, event):
        self.parent().fZone=False
        return QtGui.QDialog.closeEvent(self, event)

    def retranslateUi(self):
        self.setWindowTitle(_translate("funcZoneDialog", "نمایش پهنه و ضابطه", None))
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


    def extResult(self,objList,resList):
        for i in range(len(objList)):
            try:
                val=self.parent().Result[resList[i]]
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

    def setValues(self):
        self.setValues2()
        if self.where == 0:
            self.extResult([self.lblRainValue,self.lblEarthquakeValue,self.lblLandslideValue,self.lblFloodValue,self.lblIceValue,self.lblDroughtValue,self.lblTunderValue],[("Hazards_North","R"),("Hazards_North","Q"),("Hazards_North","L"),("Hazards_North","F"),("Hazards_North","I"),("Hazards_North","K"),("Hazards_North","S")])
        else:
            self.extResult([self.lblRainValue,self.lblEarthquakeValue,self.lblLandslideValue,self.lblDroughtValue,self.lblTunderValue],[("Hazards_South","R"),("Hazards_South","Q"),("Hazards_South","L"),("Hazards_South","K"),("Hazards_South","S")])


    def setValues2(self):

        if self.where == 0:
            self.lblZoneCodeValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Zoning_North","Result")]), None))
            self.lblZoneNameValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Zoning_North","Name")]), None))
            self.lblDetailsValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("ManageB_North","name")]), None))
            self.lblManageLawsValue.setText(_translate("funcZoneDialog",  str(self.parent().Result[("ManageB_North","MC")]), None))

##            self.lblRainValue.setText(_translate("funcZoneDialog",  str(self.parent().Result[("Hazards_North","R")]), None))
##            self.lblEarthquakeValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_North","Q")]), None))
##            self.lblLandslideValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_North","L")]), None))
##            self.lblFloodValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_North","F")]), None))
##            self.lblIceValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_North","I")]), None))
##            self.lblDroughtValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_North","K")]), None))
##            self.lblTunderValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_North","S")]), None))
        elif self.where == 1:
            self.lblZoneCodeValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Zoning_South","Result")]), None))
            self.lblZoneNameValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Zoning_South","Name")]), None))
            self.lblDetailsValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("ManageB_South","Name")]), None))
            self.lblManageLawsValue.setText(_translate("funcZoneDialog",  str(str(self.parent().Result[("ManageB_South","MC")])), None))

##            self.lblRainValue.setText(_translate("funcZoneDialog",  str(self.parent().Result[("Hazards_South","R")]), None))
##            self.lblEarthquakeValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_South","Q")]), None))
##            self.lblLandslideValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_South","L")]), None))
##            self.lblDroughtValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_South","K")]), None))
##            self.lblTunderValue.setText(_translate("funcZoneDialog", str(self.parent().Result[("Hazards_South","S")]), None))
##

