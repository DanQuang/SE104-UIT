# Form implementation generated from reading ui file 'man_hinh_bang_admin.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_man_hinh_bang_admin(object):
    def setupUi(self, man_hinh_bang_admin):
        man_hinh_bang_admin.setObjectName("man_hinh_bang_admin")
        man_hinh_bang_admin.resize(960, 540)
        self.groupBox = QtWidgets.QGroupBox(parent=man_hinh_bang_admin)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 233, 518))
        self.groupBox.setStyleSheet("border: 3px solid rgb(0, 112, 192);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 207, 231))
        self.groupBox_4.setStyleSheet("border: None;\n"
"")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 250, 207, 101))
        self.groupBox_5.setStyleSheet("border: None;\n"
"")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.groupBox_5)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 0, 207, 101))
        self.groupBox_9.setStyleSheet("border: None;")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.thoat = QtWidgets.QPushButton(parent=self.groupBox)
        self.thoat.setGeometry(QtCore.QRect(30, 420, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thoat.sizePolicy().hasHeightForWidth())
        self.thoat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        self.thoat.setFont(font)
        self.thoat.setStyleSheet("border: 3px solid rgb(0,0,0);\n"
"background-color: rgb(85, 170, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icon/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.thoat.setIcon(icon)
        self.thoat.setObjectName("thoat")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=man_hinh_bang_admin)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 698, 518))
        self.groupBox_2.setStyleSheet("border: 3px solid rgb(0, 112, 192);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_3.setStyleSheet("border: None;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.groupBox_3)
        self.groupBox_7.setGeometry(QtCore.QRect(170, 420, 511, 81))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.sua = QtWidgets.QPushButton(parent=self.groupBox_7)
        self.sua.setGeometry(QtCore.QRect(360, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        self.sua.setFont(font)
        self.sua.setStyleSheet("background-color: rgba(46, 82, 101, 200);\n"
"background-color: rgb(85, 170, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../icon/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.sua.setIcon(icon1)
        self.sua.setObjectName("sua")
        self.danh_sach_admin = QtWidgets.QTableWidget(parent=self.groupBox_3)
        self.danh_sach_admin.setGeometry(QtCore.QRect(10, 60, 651, 351))
        self.danh_sach_admin.setStyleSheet("border: 1px solid rgb(148, 148, 148);\n"
"border-radius: 10px")
        self.danh_sach_admin.setObjectName("danh_sach_admin")
        self.danh_sach_admin.setColumnCount(0)
        self.danh_sach_admin.setRowCount(0)
        self.danh_sach_admin.verticalHeader().setSortIndicatorShown(False)
        self.danh_sach_admin.verticalHeader().setStretchLastSection(False)
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(-10, 10, 691, 41))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(man_hinh_bang_admin)
        QtCore.QMetaObject.connectSlotsByName(man_hinh_bang_admin)

    def retranslateUi(self, man_hinh_bang_admin):
        _translate = QtCore.QCoreApplication.translate
        man_hinh_bang_admin.setWindowTitle(_translate("man_hinh_bang_admin", "Form"))
        self.thoat.setText(_translate("man_hinh_bang_admin", "Thoát"))
        self.sua.setText(_translate("man_hinh_bang_admin", "Sửa"))
        self.textEdit.setHtml(_translate("man_hinh_bang_admin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">TÀI KHOẢN ADMIN</span></p></body></html>"))