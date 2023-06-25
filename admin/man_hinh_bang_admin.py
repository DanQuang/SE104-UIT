from admin.ui_man_hinh_bang_admin import Ui_man_hinh_bang_admin
from admin.man_hinh_sua_admin import Man_hinh_sua_admin
from PyQt6 import QtWidgets

class Man_hinh_bang_admin(QtWidgets.QWidget, Ui_man_hinh_bang_admin):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.conn.cursor()
        self.setFixedSize(960, 540)

        self.ManHinhSuaAdmin = Man_hinh_sua_admin(self)

        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)    

    def Thoat(self):
        self.close()

    def Sua(self):
        self.ManHinhSuaAdmin.DatMacDinh()
        self.ManHinhSuaAdmin.show()

    def DatMacDinh(self):
        self.danh_sach_admin.setColumnCount(3)
        self.danh_sach_admin.setHorizontalHeaderLabels(["Mã admin","Tên tài khoản", "Mật khẩu"])
        self.danh_sach_admin.setColumnWidth(0, 150)
        self.danh_sach_admin.setColumnWidth(1, 250)
        self.danh_sach_admin.setColumnWidth(2, 250)
        
        self.danh_sach_admin.clearContents()
        self.danh_sach_admin.setRowCount(0)

        # Lấy danh sách năm học
        command = """select MaAdmin, TenTaiKhoan, MatKhau
                    from ADMIN"""
        result = self.mycursor.execute(command)

        for row_number, row_data in enumerate(result):
            self.danh_sach_admin.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_admin.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
