# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formHazardDialog.ui'
#
# Created: Sat Oct 12 04:51:55 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class formHazardDialog(QtGui.QDialog):
    def __init__(self, where, parent=None):
        super(formHazardDialog,self).__init__(parent)
        self.where=where
        self.setObjectName(_fromUtf8("formHazardDialog"))
        self.resize(845, 624)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        self.setFont(font)

        col1 = QtGui.QColor(207, 209, 154)
        col2 = QtGui.QColor(236, 238, 176)
        col3 = QtGui.QColor(213, 255, 215)
        col4 = QtGui.QColor(230, 217, 255)
        col5 = QtGui.QColor(255, 245, 231)
        col6 = QtGui.QColor(254, 251, 136)

        self.setStyleSheet("QDialog { background-color: %s }" % col1.name())

        self.groupBox1 = QtGui.QGroupBox(self)
        self.groupBox1.setGeometry(QtCore.QRect(260, 0, 571, 401))
        self.groupBox1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.groupBox1.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.gridLayout = QtGui.QGridLayout(self.groupBox1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblHazards = QtGui.QLabel(self.groupBox1)
        self.lblHazards.setFrameShape(QtGui.QFrame.Box)
        self.lblHazards.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblHazards.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHazards.setObjectName(_fromUtf8("lblHazards"))
        self.lblHazards.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblHazards, 0, 0, 7, 1)
        self.lblRain = QtGui.QCheckBox(self.groupBox1)
        self.lblRain.setEnabled(True)
        self.lblRain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblRain.setChecked(True)
        self.lblRain.setObjectName(_fromUtf8("lblRain"))
        self.lblRain.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblRain, 0, 1, 1, 1)
        self.lblRainValue = QtGui.QLabel(self.groupBox1)
        self.lblRainValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblRainValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblRainValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRainValue.setObjectName(_fromUtf8("lblRainValue"))
        self.lblRainValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblRainValue, 0, 2, 1, 1)
        self.cmbRain = QtGui.QComboBox(self.groupBox1)
        self.cmbRain.setObjectName(_fromUtf8("cmbRain"))
        self.cmbRain.setStyleSheet("QComboBox { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.cmbRain, 0, 3, 1, 1)

        self.lblEarthquake = QtGui.QCheckBox(self.groupBox1)
        self.lblEarthquake.setEnabled(True)
        self.lblEarthquake.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblEarthquake.setChecked(True)
        self.lblEarthquake.setObjectName(_fromUtf8("lblEarthquake"))
        self.lblEarthquake.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblEarthquake, 1, 1, 1, 1)
        self.lblEarthquakeValue = QtGui.QLabel(self.groupBox1)
        self.lblEarthquakeValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblEarthquakeValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblEarthquakeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEarthquakeValue.setObjectName(_fromUtf8("lblEarthquakeValue"))
        self.lblEarthquakeValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblEarthquakeValue, 1, 2, 1, 1)
        self.cmbEarthquak = QtGui.QComboBox(self.groupBox1)
        self.cmbEarthquak.setObjectName(_fromUtf8("cmbEarthquak"))
        self.cmbEarthquak.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout.addWidget(self.cmbEarthquak, 1, 3, 1, 1)

        self.lblLandslide = QtGui.QCheckBox(self.groupBox1)
        self.lblLandslide.setEnabled(True)
        self.lblLandslide.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblLandslide.setChecked(True)
        self.lblLandslide.setObjectName(_fromUtf8("lblLandslide"))
        self.lblLandslide.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblLandslide, 2, 1, 1, 1)
        self.lblLandslideValue = QtGui.QLabel(self.groupBox1)
        self.lblLandslideValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblLandslideValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblLandslideValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLandslideValue.setObjectName(_fromUtf8("lblLandslideValue"))
        self.lblLandslideValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblLandslideValue, 2, 2, 1, 1)
        self.cmbLandslide = QtGui.QComboBox(self.groupBox1)
        self.cmbLandslide.setObjectName(_fromUtf8("cmbLandslide"))
        self.cmbLandslide.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout.addWidget(self.cmbLandslide, 2, 3, 1, 1)

        self.lblFlood = QtGui.QCheckBox(self.groupBox1)
        self.lblFlood.setEnabled(True)
        self.lblFlood.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblFlood.setChecked(True)
        self.lblFlood.setObjectName(_fromUtf8("lblFlood"))
        self.lblFlood.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblFlood, 3, 1, 1, 1)
        self.lblFloodValue = QtGui.QLabel(self.groupBox1)
        self.lblFloodValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblFloodValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblFloodValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFloodValue.setObjectName(_fromUtf8("lblFloodValue"))
        self.lblFloodValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblFloodValue, 3, 2, 1, 1)
        self.cmbFlood = QtGui.QComboBox(self.groupBox1)
        self.cmbFlood.setObjectName(_fromUtf8("cmbFlood"))
        self.cmbFlood.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout.addWidget(self.cmbFlood, 3, 3, 1, 1)

        self.lblIce = QtGui.QCheckBox(self.groupBox1)
        self.lblIce.setEnabled(True)
        self.lblIce.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblIce.setChecked(True)
        self.lblIce.setObjectName(_fromUtf8("lblIce"))
        self.lblIce.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblIce, 4, 1, 1, 1)
        self.lblIceValue = QtGui.QLabel(self.groupBox1)
        self.lblIceValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblIceValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIceValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIceValue.setObjectName(_fromUtf8("lblIceValue"))
        self.lblIceValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblIceValue, 4, 2, 1, 1)
        self.cmbIce = QtGui.QComboBox(self.groupBox1)
        self.cmbIce.setObjectName(_fromUtf8("cmbIce"))
        self.cmbIce.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout.addWidget(self.cmbIce, 4, 3, 1, 1)

        self.lblDrought = QtGui.QCheckBox(self.groupBox1)
        self.lblDrought.setEnabled(True)
        self.lblDrought.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblDrought.setChecked(True)
        self.lblDrought.setObjectName(_fromUtf8("lblDrought"))
        self.lblDrought.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblDrought, 5, 1, 1, 1)
        self.lblDroughtValue = QtGui.QLabel(self.groupBox1)
        self.lblDroughtValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblDroughtValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblDroughtValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDroughtValue.setObjectName(_fromUtf8("lblDroughtValue"))
        self.lblDroughtValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblDroughtValue, 5, 2, 1, 1)
        self.cmbDrought = QtGui.QComboBox(self.groupBox1)
        self.cmbDrought.setObjectName(_fromUtf8("cmbDrought"))
        self.cmbDrought.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout.addWidget(self.cmbDrought, 5, 3, 1, 1)

        self.lblTunder = QtGui.QCheckBox(self.groupBox1)
        self.lblTunder.setEnabled(True)
        self.lblTunder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTunder.setChecked(True)
        self.lblTunder.setObjectName(_fromUtf8("lblTunder"))
        self.lblTunder.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblTunder, 6, 1, 1, 1)
        self.lblTunderValue = QtGui.QLabel(self.groupBox1)
        self.lblTunderValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblTunderValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTunderValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTunderValue.setObjectName(_fromUtf8("lblTunderValue"))
        self.lblTunderValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblTunderValue, 6, 2, 1, 1)
        self.cmbTunder = QtGui.QComboBox(self.groupBox1)
        self.cmbTunder.setObjectName(_fromUtf8("cmbTunder"))
        self.cmbTunder.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout.addWidget(self.cmbTunder, 6, 3, 1, 1)
        self.lblAmenity = QtGui.QCheckBox(self.groupBox1)
        self.lblAmenity.setEnabled(True)
        self.lblAmenity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAmenity.setChecked(False)
        self.lblAmenity.setObjectName(_fromUtf8("lblAmenity"))
        self.lblAmenity.setStyleSheet("QCheckBox { background-color: %s }" % col6.name())

        self.gridLayout.addWidget(self.lblAmenity, 7, 1, 1, 1)
        self.lblAmenityValue = QtGui.QComboBox(self.groupBox1)
        self.lblAmenityValue.setObjectName(_fromUtf8("lblAmenityValue"))
        self.lblAmenityValue.setStyleSheet("QComboBox { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblAmenityValue, 7, 2, 1, 1)
        self.cmbRain_8 = QtGui.QComboBox(self.groupBox1)
        self.cmbRain_8.setObjectName(_fromUtf8("cmbRain_8"))
        self.cmbRain_8.setStyleSheet("QComboBox { background-color: %s }" % col5.name())
        self.gridLayout.addWidget(self.cmbRain_8, 7, 3, 1, 1)
        self.lbl = QtGui.QLabel(self)
        self.lbl.setGeometry(QtCore.QRect(2, 10, 251, 621))
        self.lbl.setObjectName(_fromUtf8("graphicsView"))
        pixmap1=QtGui.QPixmap("Icons/iczm_img1.png")
        self.lbl.setScaledContents(True)
        self.lbl.setPixmap(pixmap1)

        self.groupBox2 = QtGui.QGroupBox(self)
        self.groupBox2.setGeometry(QtCore.QRect(260, 440, 571, 181))
        self.groupBox2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.groupBox2.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.btnHazardCalculate = QtGui.QPushButton(self.groupBox2)
        self.btnHazardCalculate.setGeometry(QtCore.QRect(10, 20, 221, 151))
        self.btnHazardCalculate.setObjectName(_fromUtf8("btnHazardCalculate"))
        self.btnHazardCalculate.setStyleSheet("QPushButton { background-color: %s }" % col4.name())

        self.lblHazardValue = QtGui.QLabel(self.groupBox2)
        self.lblHazardValue.setGeometry(QtCore.QRect(240, 56, 321, 81))
        self.lblHazardValue.setStyleSheet("QLabel { background-color: %s }" % col3.name())

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblHazardValue.setFont(font)
        self.lblHazardValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblHazardValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblHazardValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHazardValue.setObjectName(_fromUtf8("lblHazardValue"))

        QtCore.QObject.connect(self.btnHazardCalculate, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hazardCalculate)
        QtCore.QMetaObject.connectSlotsByName(self)


        self.retranslateUi()
        self.setValues()
        QtCore.QMetaObject.connectSlotsByName(self)

##        txtNo=_translate("formHazardDialog", "بدون اهمیت", None, QApplication.UnicodeUTF8)
##        txtLow=_translate("formHazardDialog", "کم اهمیت", None, QApplication.UnicodeUTF8)
##        txtMeddium=_translate("formHazardDialog", "با اهمیت متوسط", None, QApplication.UnicodeUTF8)
##        txtHigh=_translate("formHazardDialog", "با اهمیت زیاد", None, QApplication.UnicodeUTF8)

        txtNo=_translate("formHazardDialog", "بدون اهمیت", None)
        txtLow=_translate("formHazardDialog", "کم اهمیت", None)
        txtMeddium=_translate("formHazardDialog", "با اهمیت متوسط", None)
        txtHigh=_translate("formHazardDialog", "با اهمیت زیاد", None)

        self.cmbRain.addItem(txtNo)
        self.cmbRain.addItem(txtLow)
        self.cmbRain.addItem(txtMeddium)
        self.cmbRain.addItem(txtHigh)

        self.cmbEarthquak.addItem(txtNo)
        self.cmbEarthquak.addItem(txtLow)
        self.cmbEarthquak.addItem(txtMeddium)
        self.cmbEarthquak.addItem(txtHigh)

        self.cmbLandslide.addItem(txtNo)
        self.cmbLandslide.addItem(txtLow)
        self.cmbLandslide.addItem(txtMeddium)
        self.cmbLandslide.addItem(txtHigh)


        self.cmbFlood.addItem(txtNo)
        self.cmbFlood.addItem(txtLow)
        self.cmbFlood.addItem(txtMeddium)
        self.cmbFlood.addItem(txtHigh)

        self.cmbIce.addItem(txtNo)
        self.cmbIce.addItem(txtLow)
        self.cmbIce.addItem(txtMeddium)
        self.cmbIce.addItem(txtHigh)

        self.cmbDrought.addItem(txtNo)
        self.cmbDrought.addItem(txtLow)
        self.cmbDrought.addItem(txtMeddium)
        self.cmbDrought.addItem(txtHigh)


        self.cmbTunder.addItem(txtNo)
        self.cmbTunder.addItem(txtLow)
        self.cmbTunder.addItem(txtMeddium)
        self.cmbTunder.addItem(txtHigh)

        self.cmbRain_8.addItem(txtNo)
        self.cmbRain_8.addItem(txtLow)
        self.cmbRain_8.addItem(txtMeddium)
        self.cmbRain_8.addItem(txtHigh)

        self.lblAmenityValue.addItem(_translate("formHazardDialog", "فاقد خطر", None))
        self.lblAmenityValue.addItem(_translate("formHazardDialog", "خطرکم", None))
        self.lblAmenityValue.addItem(_translate("formHazardDialog", "خطر متوسط", None))
        self.lblAmenityValue.addItem(_translate("formHazardDialog", "خطر زیاد", None))

    def hazardCalculate(self):
        if self.where == 0:
            objList=[self.lblRain,self.lblEarthquake,self.lblLandslide,self.lblFlood,self.lblIce,self.lblDrought,self.lblTunder]
            objListWeight=[self.cmbRain,self.cmbEarthquak,self.cmbLandslide,self.cmbFlood,self.cmbIce,self.cmbDrought,self.cmbTunder]
            resList = [("Hazards_North","R"),("Hazards_North","Q"),("Hazards_North","L"),("Hazards_North","F"),("Hazards_North","I"),("Hazards_North","K"),("Hazards_North","S")]
        else:
            objList=[self.lblRain,self.lblEarthquake,self.lblLandslide,self.lblDrought,self.lblTunder]
            objListWeight=[self.cmbRain,self.cmbEarthquak,self.cmbLandslide,self.cmbDrought,self.cmbTunder]
            resList = [("Hazards_South","R"),("Hazards_South","Q"),("Hazards_South","L"),("Hazards_South","K"),("Hazards_South","S")]


        vals=[]
        weights=[]
        for i in range(len(objList)):
            if objList[i].checkState() == QtCore.Qt.Checked:
                try:
                    vals.append(self.parent().Result[resList[i]])
                    weights.append(objListWeight[i].currentIndex())
                except:
                    pass
        if self.lblAmenity.checkState() == QtCore.Qt.Checked:
                vals.append(self.lblAmenityValue.currentIndex())
                weights.append(self.cmbRain_8.currentIndex())
        totalHazard=0
        for i in range(len(vals)):
            totalHazard+=vals[i]*weights[i]
        totalHazard=round(totalHazard/(len(weights)*9.0) * 100,2)
        self.lblHazardValue.setText(str(totalHazard)+' %')






    def retranslateUi(self):
        self.setWindowTitle(_translate("formHazardDialog", "مخاطرات", None))
        self.groupBox1.setTitle(_translate("formHazardDialog", "مخاطرات", None))
        self.lblHazards.setText(_translate("formHazardDialog", "مخاطرات", None))
        self.lblRain.setText(_translate("formHazardDialog", "باران", None))
        self.lblRainValue.setText(_translate("formHazardDialog", "-", None))
        self.lblEarthquake.setText(_translate("formHazardDialog", "زلزله", None))
        self.lblEarthquakeValue.setText(_translate("formHazardDialog", "-", None))
        self.lblLandslide.setText(_translate("formHazardDialog", "رانش", None))
        self.lblLandslideValue.setText(_translate("formHazardDialog", "-", None))
        self.lblFlood.setText(_translate("formHazardDialog", "سیل", None))
        self.lblFloodValue.setText(_translate("formHazardDialog", "-", None))
        self.lblIce.setText(_translate("formHazardDialog", "یخبندان", None))
        self.lblIceValue.setText(_translate("formHazardDialog", "-", None))
        self.lblDrought.setText(_translate("formHazardDialog", "خشکسالی", None))
        self.lblDroughtValue.setText(_translate("formHazardDialog", "-", None))
        self.lblTunder.setText(_translate("formHazardDialog", "طوفان", None))
        self.lblTunderValue.setText(_translate("formHazardDialog", "-", None))
        self.lblAmenity.setText(_translate("formHazardDialog", "امنیتی", None))
        self.groupBox2.setTitle(_translate("formHazardDialog", "محاسبه برآیند مخاطرات", None))
        self.btnHazardCalculate.setText(_translate("formHazardDialog", "برآیند مخاطرات", None))
        self.lblHazardValue.setText(_translate("formHazardDialog", "0", None))

    def extResult(self,objList,resList):
        for i in range(len(objList)):
            try:
                val=self.parent().Result[resList[i]]
            except:
                val=9

            if val == 0:
                objList[i].setText(_translate("formHazardDialog", "فاقد خطر", None))
            elif val == 1:
                objList[i].setText(_translate("formHazardDialog", "خطرکم", None))
            elif val == 2:
                objList[i].setText(_translate("formHazardDialog", "خطر متوسط", None))
            elif val == 3:
                objList[i].setText(_translate("formHazardDialog", "خطر زیاد", None))
            else:
                objList[i].setText("-")

    def setValues(self):
        if self.where == 0:
            self.extResult([self.lblRainValue,self.lblEarthquakeValue,self.lblLandslideValue,self.lblFloodValue,self.lblIceValue,self.lblDroughtValue,self.lblTunderValue],[("Hazards_North","R"),("Hazards_North","Q"),("Hazards_North","L"),("Hazards_North","F"),("Hazards_North","I"),("Hazards_North","K"),("Hazards_North","S")])
        else:
            self.extResult([self.lblRainValue,self.lblEarthquakeValue,self.lblLandslideValue,self.lblDroughtValue,self.lblTunderValue],[("Hazards_South","R"),("Hazards_South","Q"),("Hazards_South","L"),("Hazards_South","K"),("Hazards_South","S")])

    def closeEvent(self, event):
        self.parent().fRisk=False
        return QtGui.QDialog.closeEvent(self, event)


##    def setValues1(self):
##
##        if self.where == 0:
##          #  vR=self.parent().Result[("Hazards_North","R")]
##           # if vR == 0:
##
##            self.lblRainValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_North","R")]), None))
##            self.lblEarthquakeValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_North","Q")]), None))
##            self.lblLandslideValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_North","L")]), None))
##            self.lblFloodValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_North","F")]), None))
##            self.lblIceValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_North","I")]), None))
##            self.lblDroughtValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_North","K")]), None))
##            self.lblTunderValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_North","S")]), None))
##
##        elif self.where == 1:
##            self.lblRainValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_South","R")]), None))
##            self.lblEarthquakeValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_South","Q")]), None))
##            self.lblLandslideValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_South","L")]), None))
##            self.lblDroughtValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_South","K")]), None))
##            self.lblTunderValue.setText(_translate("formHazardDialog", str(self.parent().Result[("Hazards_South","S")]), None))

