# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formEcologic.ui'
#
# Created: Sat Oct 12 04:51:38 2013
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

class formEcologicDialog(QtGui.QDialog):
    def __init__(self, where, parent=None):
        super(formEcologicDialog,self).__init__(parent)
        self.where=where
        self.setObjectName(_fromUtf8("formEcologicDialog"))
        self.resize(612, 490)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)

        col1 = QtGui.QColor(207, 209, 154)
        col2 = QtGui.QColor(236, 238, 176)
        #col3 = QtGui.QColor(241, 241, 149)
        col4 = QtGui.QColor(230, 217, 255)
        col5 = QtGui.QColor(255, 245, 231)

        self.setStyleSheet("QDialog { background-color: %s }" % col1.name())
        self.setFont(font)
        self.groupBox1 = QtGui.QGroupBox(self)
        self.groupBox1.setGeometry(QtCore.QRect(10, 10, 391, 321))
        self.groupBox1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))

        self.groupBox1.setStyleSheet("QGroupBox { background-color: %s }" % col2.name())

        self.gridLayout = QtGui.QGridLayout(self.groupBox1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblResidential = QtGui.QLabel(self.groupBox1)
        self.lblResidential.setFrameShape(QtGui.QFrame.Box)
        self.lblResidential.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResidential.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResidential.setObjectName(_fromUtf8("lblResidential"))

        self.lblResidential.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblResidential, 4, 0, 1, 1)
        self.lblIndust = QtGui.QLabel(self.groupBox1)
        self.lblIndust.setFrameShape(QtGui.QFrame.Box)
        self.lblIndust.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndust.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndust.setObjectName(_fromUtf8("lblIndust"))
        self.lblIndust.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblIndust, 2, 0, 1, 1)
        self.lblConservValue = QtGui.QLabel(self.groupBox1)
        self.lblConservValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblConservValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblConservValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConservValue.setObjectName(_fromUtf8("lblConservValue"))
        self.lblConservValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblConservValue, 3, 1, 1, 1)
        self.lblConsetv = QtGui.QLabel(self.groupBox1)
        self.lblConsetv.setFrameShape(QtGui.QFrame.Box)
        self.lblConsetv.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblConsetv.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConsetv.setObjectName(_fromUtf8("lblConsetv"))
        self.lblConsetv.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblConsetv, 3, 0, 1, 1)
        self.lblTourismValue = QtGui.QLabel(self.groupBox1)
        self.lblTourismValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblTourismValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourismValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourismValue.setObjectName(_fromUtf8("lblTourismValue"))
        self.lblTourismValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblTourismValue, 1, 1, 1, 1)
        self.lblAgriValue = QtGui.QLabel(self.groupBox1)
        self.lblAgriValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblAgriValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgriValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgriValue.setObjectName(_fromUtf8("lblAgriValue"))
        self.lblAgriValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblAgriValue, 0, 1, 1, 1)
        self.lblIndustValue = QtGui.QLabel(self.groupBox1)
        self.lblIndustValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblIndustValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblIndustValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndustValue.setObjectName(_fromUtf8("lblIndustValue"))
        self.lblIndustValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblIndustValue, 2, 1, 1, 1)
        self.lblAgri = QtGui.QLabel(self.groupBox1)
        self.lblAgri.setFrameShape(QtGui.QFrame.Box)
        self.lblAgri.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblAgri.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAgri.setObjectName(_fromUtf8("lblAgri"))
        self.lblAgri.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblAgri, 0, 0, 1, 1)
        self.lblResidentialValue = QtGui.QLabel(self.groupBox1)
        self.lblResidentialValue.setFrameShape(QtGui.QFrame.Panel)
        self.lblResidentialValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblResidentialValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResidentialValue.setObjectName(_fromUtf8("lblResidentialValue"))
        self.lblResidentialValue.setStyleSheet("QLabel { background-color: %s }" % col5.name())

        self.gridLayout.addWidget(self.lblResidentialValue, 4, 1, 1, 1)
        self.lblTourism = QtGui.QLabel(self.groupBox1)
        self.lblTourism.setFrameShape(QtGui.QFrame.Box)
        self.lblTourism.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTourism.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTourism.setObjectName(_fromUtf8("lblTourism"))
        self.lblTourism.setStyleSheet("QLabel { background-color: %s }" % col4.name())

        self.gridLayout.addWidget(self.lblTourism, 1, 0, 1, 1)
        #pixmap1=QtGui.QPixmap("Icons/iczm_img1.png")
        pixmap1=QtGui.QPixmap("Icons/Software_img2.png")
        pixmap2=QtGui.QPixmap("Icons/iczm_img2.png")
        self.lbl1 = QtGui.QLabel(self)
        self.lbl1.setGeometry(QtCore.QRect(410, 20, 191, 461))
        self.lbl1.setObjectName(_fromUtf8("graphic1"))
        self.lbl1.setScaledContents(True)
        self.lbl1.setPixmap(pixmap1)
        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setGeometry(QtCore.QRect(10, 340, 391, 141))
        self.lbl2.setObjectName(_fromUtf8("graphic2"))
        self.lbl2.setScaledContents(True)
        self.lbl2.setPixmap(pixmap2)
        self.retranslateUi()
        self.setValues()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("formEcologicDialog", "نمایش توان اکولوژیک", None))
        self.groupBox1.setTitle(_translate("formEcologicDialog", "توان اکولوژیک", None))
        self.lblResidential.setText(_translate("formEcologicDialog", "شهری", None))
        self.lblIndust.setText(_translate("formEcologicDialog", "صنعتی", None))
        self.lblConservValue.setText(_translate("formEcologicDialog", "-", None))
        self.lblConsetv.setText(_translate("formEcologicDialog", "حفاظتی", None))
        self.lblTourismValue.setText(_translate("formEcologicDialog", "-", None))
        self.lblAgriValue.setText(_translate("formEcologicDialog", "-", None))
        self.lblIndustValue.setText(_translate("formEcologicDialog", "-", None))
        self.lblAgri.setText(_translate("formEcologicDialog", "کشاورزی", None))
        self.lblResidentialValue.setText(_translate("formEcologicDialog", "-", None))
        self.lblTourism.setText(_translate("formEcologicDialog", "گردشگری", None))

    def setValues(self):

        if self.where == 0:
            self.lblConservValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_North","P_Conserv")]), None))
            self.lblTourismValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_North","P_Tour")]), None))
            self.lblAgriValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_North","P_Agri")]), None))
            self.lblIndustValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_North","P_Indust")]), None))
            self.lblResidentialValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_North","P_Urban")]), None))
        elif self.where == 1:
            self.lblConservValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_South","P_Conserv")]), None))
            self.lblTourismValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_South","P_Tour")]), None))
            self.lblAgriValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_South","P_Agri")]), None))
            self.lblIndustValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_South","P_Indust")]), None))
            self.lblResidentialValue.setText(_translate("formEcologicDialog", str(self.parent().Result[("Tavan_South","P_Urban")]), None))
    def closeEvent(self, event):
        self.parent().fEcol=False
        return QtGui.QDialog.closeEvent(self, event)
