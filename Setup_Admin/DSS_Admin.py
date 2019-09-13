# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created: Sun Nov 17 04:57:44 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!
import sys, os
import shutil
from PyQt4 import QtCore, QtGui
from random import randint

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

class DSS_Admin(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(DSS_Admin,self).__init__(parent)

        self.setObjectName(_fromUtf8("DSS_Admin"))
        self.resize(536, 456)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.list1 = QtGui.QListWidget(self.centralwidget)
        self.list1.setObjectName(_fromUtf8("list1"))
        self.horizontalLayout_2.addWidget(self.list1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.verticalLayout.addWidget(self.btn1)
        self.btn2 = QtGui.QPushButton(self.centralwidget)
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.verticalLayout.addWidget(self.btn2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.list2 = QtGui.QListWidget(self.centralwidget)
        self.list2.setObjectName(_fromUtf8("list2"))
        self.horizontalLayout_2.addWidget(self.list2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimum(1)
        self.progressBar.setMaximum(100)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.SetupProject = QtGui.QPushButton(self.centralwidget)
        self.SetupProject.setObjectName(_fromUtf8("SetupProject"))
        self.verticalLayout_2.addWidget(self.SetupProject)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 2)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        QtCore.QObject.connect(self.btn1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.itemMove)
        QtCore.QObject.connect(self.btn2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.itemMove2)
        QtCore.QObject.connect(self.SetupProject, QtCore.SIGNAL(_fromUtf8("clicked()")), self.setupProject)
        self.setupList()

    def setupList(self):
        self.list1.addItem('گلستان'.decode('utf-8'))
        self.list1.addItem('مازندران'.decode('utf-8'))
        self.list1.addItem('گیلان'.decode('utf-8'))
        self.list1.addItem('خوزستان'.decode('utf-8'))
        self.list1.addItem('بوشهر'.decode('utf-8'))
        self.list1.addItem('هرمزگان'.decode('utf-8'))
        self.list1.addItem('سیستان و بلوچستان'.decode('utf-8'))
        self.list1.addItem('استانهای شمالی'.decode('utf-8'))
        self.list1.addItem('استانهای جنوبی'.decode('utf-8'))
    def itemMove(self):

        if len(self.list1.selectedItems()) > 0:

            self.list2.addItem(self.list1.currentItem().text())
            self.list1.takeItem(self.list1.currentIndex().row())
    def itemMove2(self):

        if len(self.list2.selectedItems()) > 0:

            self.list1.addItem(self.list2.currentItem().text())
            self.list2.takeItem(self.list2.currentIndex().row())

    def setupProject(self):
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        if len(str(self.lineEdit_2.text())) < 4 or len(str(self.lineEdit_2.text())) > 8:
            txtMapWarning=QtGui.QApplication.translate("DSS_Admin", "طول کلمه رمز باید بین 4 تا 8 کاراکتر باشد", None, QtGui.QApplication.UnicodeUTF8)
            txtMapWarningTitle=QtGui.QApplication.translate("DSS_Admin", "خطا", None, QtGui.QApplication.UnicodeUTF8)
            QtGui.QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)

        else:
            try:
                self.projectName=str(self.lineEdit.text())
            except:
                txtMapWarning=QtGui.QApplication.translate("DSS_Admin", "لازم است برای پروژه یک نام به صورت لاتین وارد گردد", None, QtGui.QApplication.UnicodeUTF8)
                txtMapWarningTitle=QtGui.QApplication.translate("DSS_Admin", "خطا", None, QtGui.QApplication.UnicodeUTF8)
                QtGui.QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)

            if self.projectName == '':
                    txtMapWarning=QtGui.QApplication.translate("DSS_Admin", "لازم است برای پروژه یک نام به صورت لاتین وارد گردد", None, QtGui.QApplication.UnicodeUTF8)
                    txtMapWarningTitle=QtGui.QApplication.translate("DSS_Admin", "خطا", None, QtGui.QApplication.UnicodeUTF8)
                    QtGui.QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)
            else:
                if os.path.exists('Projects/'+self.projectName):
                    shutil.rmtree('Projects/'+self.projectName)
                self.provinceList=[]
                if self.list2.count() > 0:
                    for i in range(self.list2.count()):
                        if unicode(self.list2.item(i).text()) == 'سیستان و بلوچستان'.decode('utf-8'):
                            self.provinceList.append('Sistan')
                        elif unicode(self.list2.item(i).text()) == 'گلستان'.decode('utf-8'):
                             self.provinceList.append('Golestan')

                        elif unicode(self.list2.item(i).text()) == 'مازندران'.decode('utf-8'):
                             self.provinceList.append('Mazandaran')
                        elif unicode(self.list2.item(i).text()) == 'خوزستان'.decode('utf-8'):
                             self.provinceList.append('Khozestan')
                        elif unicode(self.list2.item(i).text()) == 'گیلان'.decode('utf-8'):
                             self.provinceList.append('Gilan')
                        elif unicode(self.list2.item(i).text()) == 'بوشهر'.decode('utf-8'):
                             self.provinceList.append('Boushehr')
                        elif unicode(self.list2.item(i).text()) == 'هرمزگان'.decode('utf-8'):
                             self.provinceList.append('Hormozgan')
                        elif unicode(self.list2.item(i).text()) == 'استانهای شمالی'.decode('utf-8'):
                             self.provinceList.append('North')
                        elif unicode(self.list2.item(i).text()) == 'استانهای جنوبی'.decode('utf-8'):
                             self.provinceList.append('South')

                    os.makedirs('Projects/'+self.projectName+'/Settings',0755)
                    f_settings=open('Projects/'+self.projectName+'/Settings/config.ini','w')
                    f_settings.writelines(['provinces:'])
                    for i in range(len(self.provinceList)):
                        item=self.provinceList[i]
                        if i == 0:
                            f_settings.writelines([' '])
                            f_settings.writelines([item])

                        else:
                            f_settings.writelines([', '])
                            f_settings.writelines([item])

                    f_settings.writelines(['\n'])
                    f_settings.writelines(['lastOpenPath: \n'])
                    f_settings.writelines(['passCheck: True'])
                    f_settings.close()
                    f_settings=open('Projects/'+self.projectName+'/Settings/key','w')
                    f_settings.writelines([self.passGenerate()])
                    f_settings.close()
                    self.copyFiles()
                    self.progressBar.setValue(100)
                    QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                    txtMapWarning=QtGui.QApplication.translate("DSS_Admin", "پروژه با موفقیت ایجاد گردید", None, QtGui.QApplication.UnicodeUTF8)
                    txtMapWarningTitle=QtGui.QApplication.translate("DSS_Admin", "توجه", None, QtGui.QApplication.UnicodeUTF8)
                    QtGui.QMessageBox.information(self,txtMapWarningTitle,txtMapWarning)


                else:

                    os.makedirs('Projects/'+self.projectName,0755)
                    f_settings=open('Projects/'+self.projectName+'/key','w')
                    f_settings.writelines([self.passGenerate()])
                    f_settings.close()
                    self.progressBar.setValue(100)
                    QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                    txtMapWarning=QtGui.QApplication.translate("DSS_Admin", "به دلیل اینکه هیچ استانی انتخاب نشد، تنها فایل لایسنس در فولدر پروژه مشخص شده ایجاد گردید", None, QtGui.QApplication.UnicodeUTF8)
                    txtMapWarningTitle=QtGui.QApplication.translate("DSS_Admin", "توجه", None, QtGui.QApplication.UnicodeUTF8)
                    QtGui.QMessageBox.warning(self,txtMapWarningTitle,txtMapWarning)

        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))





    def copyFiles(self):
##        num=len(os.listdir('Icons'))
##        val=0
##        p=3.0 / num
##
##        os.makedirs('Projects/'+self.projectName+'/Icons',0755)
##        src_files = os.listdir('Icons')
##        for file_name in src_files:
##            full_file_name = os.path.join('Icons', file_name)
##            if (os.path.isfile(full_file_name)):
##                shutil.copy(full_file_name, 'Projects/'+self.projectName+'/Icons')
##            val+=p
##            self.progressBar.setValue(val)
##
##        num=len(os.listdir('Helps'))
##        p=3.0 / num
##        os.makedirs('Projects/'+self.projectName+'/Helps',0755)
##        src_files = os.listdir('Helps')
##        for file_name in src_files:
##            full_file_name = os.path.join('Helps', file_name)
##            if (os.path.isfile(full_file_name)):
##                shutil.copy(full_file_name, 'Projects/'+self.projectName+'/Helps')
##            val+=p
##            self.progressBar.setValue(val)
##
        val=0
        num=len(self.provinceList) * 50
        p=96 / num
        for item in self.provinceList:
            prv=item.split(',')[0].strip()
            if prv == 'Sistan':
                prv='Sistan_Balouchestan'
            os.makedirs('Projects/'+self.projectName+'/Data/_'+prv,0755)
            src_files = os.listdir('Data/_'+prv)
            for file_name in src_files:
                full_file_name = os.path.join('Data/_'+prv, file_name)
                if (os.path.isfile(full_file_name)):
                    shutil.copy(full_file_name, 'Projects/'+self.projectName+'/Data/_'+prv)
                    val+=p
                    if val >= 96:
                        val = 96
                    self.progressBar.setValue(val)
        #os.makedirs('Projects/'+self.projectName+'/temp',0755)
        full_file_name = os.path.join('Settings', 'frp')

        if (os.path.isfile(full_file_name)):
                shutil.copy(full_file_name, 'Projects/'+self.projectName+'/Settings')




    def passGenerate(self):
        hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','#','&','$','A','X','Y','Z','H','S','I','N','%','@']
        digit_array = []
        for p in str(self.lineEdit_2.text()):
            for i in range(10):
                digit_array.append(hex_digits[randint(0,32)])
            digit_array.append(p)
        return ''.join(digit_array)




    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "راهبر سامانه پشتیبان تصمیم گیری", None))
        self.label_2.setText(_translate("MainWindow", "مدیریت کاربران و راهبری سامانه پشتیبان تصمیم گیری مدیریت یکپارچه مناطق ساحلی", None))
        self.label.setText(_translate("MainWindow", "نام  پروژه", None))
        self.label_3.setText(_translate("MainWindow", "گروه های اطلاعاتی موجود به تفکیک استان یا ناحیه", None))
        self.label_5.setText(_translate("MainWindow", "گروه های اطلاعاتی انتخاب شده برای پروژه", None))
        self.btn1.setText(_translate("MainWindow", ">>", None))
        self.btn2.setText(_translate("MainWindow", "<<", None))
        self.label_4.setText(_translate("MainWindow", "ایجاد نام کاربری برای پروژه", None))
        self.SetupProject.setText(_translate("MainWindow", "ایجاد پروژه", None))

def main():
    app=QtGui.QApplication([])
    app.setOrganizationName("Sap Consulting Engineers Co.")
    app.setOrganizationDomain("r-gis.net")
    app.setApplicationName("Administrator of ICZM DSS")
    app.setWindowIcon(QtGui.QIcon("Icons/admin.png"))
    w=DSS_Admin()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()