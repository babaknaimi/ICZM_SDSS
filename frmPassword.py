 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPassword.ui'
#
# Created: Sun Nov 17 08:56:02 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
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

class frmPassWord(QtGui.QDialog):
    closeApp = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        super(frmPassWord,self).__init__(parent)
        self.closeApp.connect(self.close)
        self.PassWord=False
        self.setObjectName(_fromUtf8("frmPassWord"))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(302, 160)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.userPass = QtGui.QLineEdit(self)
        self.userPass.setObjectName(_fromUtf8("userPass"))
        self.userPass.setEchoMode(QtGui.QLineEdit.Password)
        self.horizontalLayout.addWidget(self.userPass)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.passCheck = QtGui.QCheckBox(self)
        self.passCheck.setObjectName(_fromUtf8("passCheck"))
        self.horizontalLayout_2.addWidget(self.passCheck)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.passControl)


    def retranslateUi(self):
        self.setWindowTitle(_translate("frmPassWord", "Form", None))
        self.label.setText(_translate("frmPassWord", "کلمه عبور را وارد نمایید:", None))
        self.label_2.setText(_translate("frmPassWord", "Password:", None))
        self.passCheck.setText(_translate("frmPassWord", "کلمه عبور را به خاطر بسپار", None))
        self.pushButton.setText(_translate("frmPassWord", "Ok", None))

    def passControl(self):
        if not os.path.exists('Settings/key'):
            txtMapWarning=QtGui.QApplication.translate("iczmDSS", "این نرم افزار نیاز به فعال سازی از طریق فایل لایسنس دارد", None, QtGui.QApplication.UnicodeUTF8)
            txtMapWarningTitle=QtGui.QApplication.translate("iczmDSS", "خطا", None, QtGui.QApplication.UnicodeUTF8)
            QtGui.QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)
        else:
            f=open('Settings/key','r')
            l=f.readlines()
            f.close()
            n = len(str(l[0]).strip()) / 10
            p=[]
            for i in range(n):
                p.append((i+1)*10 +i)

            pa=[l[0][i] for i in p]
            pa=''.join(pa)

            if  str(self.userPass.text()) == pa:
                self.PassWord=True
                f=open('Settings/config.ini','r')
                lines=f.readlines()
                f.close()
                f=open('Settings/config.ini','w')
                p=False
                for l in lines:
                    if l.split(':')[0].strip() == 'passCheck':
                        p=True
                        if self.passCheck.checkState() == QtCore.Qt.Checked:

                            f.writelines(['passCheck: False'])
                        else:
                            f.writelines(['passCheck: True'])

                    else:
                        f.writelines([l])
                if p:
                    f.close()
                else:
                    if self.passCheck.checkState() == QtCore.Qt.Checked:
                        f.writelines(['passCheck: False'])

                    else:
                        f.writelines(['passCheck: True'])


                    f.close()


                self.close()
            else:
                txtMapWarning=QtGui.QApplication.translate("frmPassWord", "کلمه رمز اشتباه می باشد", None, QtGui.QApplication.UnicodeUTF8)
                txtMapWarningTitle=QtGui.QApplication.translate("frmPassWord", "خطا", None, QtGui.QApplication.UnicodeUTF8)
                QtGui.QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)
    def setPassCheck(self):
        self.PassWord=False
        f=open('Settings/config.ini','r')
        lines=f.readlines()
        f.close()
        f=open('Settings/config.ini','w')
        p=False
        for l in lines:
            if l.split(':')[0].strip() == 'passCheck':
                p=True
                f.writelines(['passCheck: True'])

            else:
                f.writelines([l])
        if p:
            f.close()
        else:
            f.writelines(['passCheck: True'])
            f.close()





    def keyPressEvent(self,event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.setPassCheck()
            self.closeApp.emit()



    def closeEvent(self, event):
        if self.PassWord:
            pass
        else:
            self.parent().close()
        return QtGui.QDialog.closeEvent(self, event)

