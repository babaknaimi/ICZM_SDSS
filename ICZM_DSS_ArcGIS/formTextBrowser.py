# -*- coding: utf-8 -*-

# ICZM DSS
# Developed By Babak Naimi (SAP Consulting Engineers Co.)
# Client: PMO
# --  Widget to display text contents


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

class formTextBrowser(QtGui.QDialog):
    def __init__(self, parent=None):
        super(formTextBrowser,self).__init__(parent)
        self.setObjectName(_fromUtf8("formTextBrowser"))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(489, 539)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(10)
        self.setFont(font)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.setToolTip(_fromUtf8(""))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("formTextBrowser", "نمایش محتوای متنی", None))


