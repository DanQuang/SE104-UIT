# Form implementation generated from reading ui file 'man_hinh_them_mon_hoc.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_man_hinh_them_mon_hoc(object):
    def setupUi(self, man_hinh_them_mon_hoc):
        man_hinh_them_mon_hoc.setObjectName("man_hinh_them_mon_hoc")
        man_hinh_them_mon_hoc.resize(400, 300)
        self.label = QtWidgets.QLabel(parent=man_hinh_them_mon_hoc)
        self.label.setGeometry(QtCore.QRect(30, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;")
        self.label.setObjectName("label")
        self.ten_mon_hoc = QtWidgets.QLineEdit(parent=man_hinh_them_mon_hoc)
        self.ten_mon_hoc.setGeometry(QtCore.QRect(170, 70, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.ten_mon_hoc.setFont(font)
        self.ten_mon_hoc.setStyleSheet("border: 2px solid rgb(0, 112, 192);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.ten_mon_hoc.setObjectName("ten_mon_hoc")
        self.label_8 = QtWidgets.QLabel(parent=man_hinh_them_mon_hoc)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.label_8.setStyleSheet("border: 2px solid rgb(0, 112, 192);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.thoat = QtWidgets.QPushButton(parent=man_hinh_them_mon_hoc)
        self.thoat.setGeometry(QtCore.QRect(280, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        self.thoat.setFont(font)
        self.thoat.setStyleSheet("border: 3px solid rgb(0,0,0);\n"
"background-color: rgb(255, 85, 0);\n"
"border-radius: 5px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/32_n.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.thoat.setIcon(icon)
        self.thoat.setObjectName("thoat")
        self.them = QtWidgets.QPushButton(parent=man_hinh_them_mon_hoc)
        self.them.setGeometry(QtCore.QRect(280, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        self.them.setFont(font)
        self.them.setStyleSheet("border: 3px solid rgb(0,0,0);\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/6_n.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.them.setIcon(icon1)
        self.them.setObjectName("them")
        self.label_8.raise_()
        self.label.raise_()
        self.ten_mon_hoc.raise_()
        self.thoat.raise_()
        self.them.raise_()

        self.retranslateUi(man_hinh_them_mon_hoc)
        QtCore.QMetaObject.connectSlotsByName(man_hinh_them_mon_hoc)

    def retranslateUi(self, man_hinh_them_mon_hoc):
        _translate = QtCore.QCoreApplication.translate
        man_hinh_them_mon_hoc.setWindowTitle(_translate("man_hinh_them_mon_hoc", "Form"))
        self.label.setText(_translate("man_hinh_them_mon_hoc", "Tên môn học: "))
        self.thoat.setText(_translate("man_hinh_them_mon_hoc", "THOÁT"))
        self.them.setText(_translate("man_hinh_them_mon_hoc", "THÊM"))
