# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmHelpView.ui'
#
# Created: Sat Nov 16 04:12:38 2013
#      by: PyQt4 UI code generator 4.10
#


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

class frmHelpView(QtGui.QDialog):
    def __init__(self, address="", parent=None):
        super(frmHelpView,self).__init__(parent)

        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(870, 700)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(self)
        self.webView.setUrl(QtCore.QUrl(address))
        self.webView.load(QtCore.QUrl(address))

        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.printButton=QtGui.QPushButton(self)
        self.printButton.setObjectName(_fromUtf8("printButton"))
        self.verticalLayout.addWidget(self.printButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.printButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printPage)
        self.webView.reload()
    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "نمایش مستندات", None))
        self.printButton.setText(_translate("Dialog", "چاپ ", None))

    def closeEvent(self, event):
        self.parent().fHlp=False
        return QtGui.QDialog.closeEvent(self, event)

    def printPage(self):
        printer=QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setFullPage(True)
        dialog = QtGui.QPrintDialog(printer, self)
        if(dialog.exec_() != QtGui.QDialog.Accepted):
             return
        self.webView.print_(printer)



from PyQt4 import QtWebKit
from PyQt4 import QtNetwork
