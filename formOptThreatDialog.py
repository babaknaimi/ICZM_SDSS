# -*- coding: utf-8 -*-

# ICZM DSS
# Developed By Babak Naimi (SAP Consulting Engineers Co.)
# Client: PMO
# --  Form Dialog to display Opportunity and Threats

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

class frmOptThreatDialog(QtGui.QDialog):
    def __init__(self, where, parent=None):
        super(frmOptThreatDialog,self).__init__(parent)
        self.where=where
        self.setObjectName(_fromUtf8("frmOptThreatDialog"))
        self.resize(791, 611)


        col1 = QtGui.QColor(207, 209, 154)
        col2 = QtGui.QColor(236, 238, 176)
        col3 = QtGui.QColor(213, 255, 215)
        col4 = QtGui.QColor(230, 217, 255)
        col5 = QtGui.QColor(255, 245, 231)
        col6 = QtGui.QColor(254, 251, 136)
        self.setStyleSheet("QDialog { background-color: %s }" % col1.name())

        self.groupBox1 = QtGui.QGroupBox(self)
        self.groupBox1.setGeometry(QtCore.QRect(397, 0, 391, 321))
        self.groupBox1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.groupBox1.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())
        self.gridLayout = QtGui.QGridLayout(self.groupBox1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblIndustValue = QtGui.QLabel(self.groupBox1)
        self.lblIndustValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblIndustValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndustValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndustValue.setObjectName(_fromUtf8("lblIndustValue"))
        self.lblIndustValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblIndustValue, 2, 1, 1, 1)
        self.lblTourismValue = QtGui.QLabel(self.groupBox1)
        self.lblTourismValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblTourismValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourismValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourismValue.setObjectName(_fromUtf8("lblTourismValue"))
        self.lblTourismValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblTourismValue, 1, 1, 1, 1)
        self.lblIndust = QtGui.QLabel(self.groupBox1)
        self.lblIndust.setFrameShape(QtGui.QFrame.Box)
        self.lblIndust.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndust.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndust.setObjectName(_fromUtf8("lblIndust"))
        self.lblIndust.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblIndust, 2, 0, 1, 1)
        self.lblResid = QtGui.QLabel(self.groupBox1)
        self.lblResid.setFrameShape(QtGui.QFrame.Box)
        self.lblResid.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResid.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResid.setObjectName(_fromUtf8("lblResid"))
        self.lblResid.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblResid, 3, 0, 1, 1)
        self.lblAgriValue = QtGui.QLabel(self.groupBox1)
        self.lblAgriValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblAgriValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgriValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgriValue.setObjectName(_fromUtf8("lblAgriValue"))
        self.lblAgriValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblAgriValue, 0, 1, 1, 1)
        self.lblResidValue = QtGui.QLabel(self.groupBox1)
        self.lblResidValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblResidValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResidValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResidValue.setObjectName(_fromUtf8("lblResidValue"))
        self.lblResidValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblResidValue, 3, 1, 1, 1)
        self.lblTourism = QtGui.QLabel(self.groupBox1)
        self.lblTourism.setFrameShape(QtGui.QFrame.Box)
        self.lblTourism.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourism.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourism.setObjectName(_fromUtf8("lblTourism"))
        self.lblTourism.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblTourism, 1, 0, 1, 1)
        self.lblAgri = QtGui.QLabel(self.groupBox1)
        self.lblAgri.setFrameShape(QtGui.QFrame.Box)
        self.lblAgri.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgri.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgri.setObjectName(_fromUtf8("lblAgri"))
        self.lblAgri.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblAgri, 0, 0, 1, 1)
        self.groupBox1_2 = QtGui.QGroupBox(self)
        self.groupBox1_2.setGeometry(QtCore.QRect(2, 0, 391, 321))
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
        #pixmap1=QtGui.QPixmap("Icons/iczm_img3.png")
        #pixmap2=QtGui.QPixmap("Icons/iczm_img2.png")
        pixmap2=QtGui.QPixmap("Icons/Software_img3.png")
        self.lbl2 = QtGui.QLabel(self)
        #self.lbl2.setGeometry(QtCore.QRect(2, 325, 551, 181))
        self.lbl2.setGeometry(QtCore.QRect(2, 325, 782, 281))
        self.lbl2.setObjectName(_fromUtf8("graphic2"))
        self.lbl1 = QtGui.QLabel(self)
        #self.lbl1.setGeometry(QtCore.QRect(556, 326, 231, 181))
        #self.lbl1.setObjectName(_fromUtf8("graphic1"))
        #self.lbl1.setScaledContents(True)
        self.lbl2.setScaledContents(True)
        #self.lbl1.setPixmap(pixmap1)
        self.lbl2.setPixmap(pixmap2)

        self.retranslateUi()
        self.setValues()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("frmOptThreatDialog", "فرصت ها و تهدید های دریایی", None))
        self.groupBox1.setTitle(_translate("frmOptThreatDialog", "تهدیدهای دریایی", None))
        self.lblIndustValue.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblTourismValue.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblIndust.setText(_translate("frmOptThreatDialog", "صنعتی", None))
        self.lblResid.setText(_translate("frmOptThreatDialog", "سکونت", None))
        self.lblAgriValue.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblResidValue.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblTourism.setText(_translate("frmOptThreatDialog", "گردشگری", None))
        self.lblAgri.setText(_translate("frmOptThreatDialog", "کشاورزی", None))
        self.groupBox1_2.setTitle(_translate("frmOptThreatDialog", "فرصتهای دریایی", None))
        self.lblTourism_2.setText(_translate("frmOptThreatDialog", "گردشگری", None))
        self.lblIndust_2.setText(_translate("frmOptThreatDialog", "صنعتی", None))
        self.lblTourismValue_2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblResid_2.setText(_translate("frmOptThreatDialog", "سکونت", None))
        self.lblResidValue_2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblAgri_2.setText(_translate("frmOptThreatDialog", "کشاورزی", None))
        self.lblIndustValue_2.setText(_translate("frmOptThreatDialog", "-", None))
        self.lblAgriValue_2.setText(_translate("frmOptThreatDialog", "-", None))

    def extResult(self,objList,resList):
        for i in range(len(objList)):
            try:
                val=self.parent().Result[resList[i]]
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

    def setValues(self):
        if self.where == 0:
            self.extResult([self.lblResidValue,self.lblTourismValue,self.lblAgriValue,self.lblIndustValue,self.lblResidValue_2,self.lblTourismValue_2,self.lblAgriValue_2,self.lblIndustValue_2],\
            [("Opportunity_North","O_Resid"),("Opportunity_North","O_Tour"),("Opportunity_North","O_Agri"),("Opportunity_North","O_Indust"),("Threat_North","T_Resid"),("Threat_North","T_Tour"),("Threat_North","T_Agri"),("Threat_North","T_Indust")])
        else:
            self.extResult([self.lblResidValue,self.lblTourismValue,self.lblAgriValue,self.lblIndustValue,self.lblResidValue_2,self.lblTourismValue_2,self.lblAgriValue_2,self.lblIndustValue_2],\
            [("Opportunity_South","O_Resid"),("Opportunity_South","O_Tour"),("Opportunity_South","O_Agri"),("Opportunity_South","O_Indust"),("Threat_South","T_Resid"),("Threat_South","T_Tour"),("Threat_South","T_Agri"),("Threat_South","T_Indust")])
    def closeEvent(self, event):
        self.parent().fOpt=False
        return QtGui.QDialog.closeEvent(self, event)


##    def setValues2(self):
##
##        if self.where == 0:
##            self.lblResidValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_North","O_Resid")]), None))
##            self.lblTourismValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_North","O_Tour")]), None))
##            self.lblAgriValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_North","O_Agri")]), None))
##            self.lblIndustValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_North","O_Indust")]), None))
##
##            self.lblResidValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_North","T_Resid")]), None))
##            self.lblTourismValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_North","T_Tour")]), None))
##            self.lblAgriValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_North","T_Agri")]), None))
##            self.lblIndustValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_North","T_Indust")]), None))
##
##
##        elif self.where == 1:
##            self.lblResidValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_South","O_Resid")]), None))
##            self.lblTourismValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_South","O_Tour")]), None))
##            self.lblAgriValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_South","O_Agri")]), None))
##            self.lblIndustValue.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Opportunity_South","O_Indust")]), None))
##
##            self.lblResidValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_South","T_Resid")]), None))
##            self.lblTourismValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_South","T_Tour")]), None))
##            self.lblAgriValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_South","T_Agri")]), None))
##            self.lblIndustValue_2.setText(_translate("frmOptThreatDialog", str(self.parent().Result[("Threat_South","T_Indust")]), None))
