from admin.ui_man_hinh_bang_giang_vien import Ui_man_hinh_bang_giang_vien
from admin.man_hinh_them_giang_vien import Man_hinh_them_giang_vien
from admin.man_hinh_sua_giang_vien import Man_hinh_sua_giang_vien
from PyQt6 import QtWidgets

class Man_hinh_bang_giang_vien(QtWidgets.QWidget, Ui_man_hinh_bang_giang_vien):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.conn.cursor()
        self.setFixedSize(960, 540)

        self.ManHinhThemGiangVien = Man_hinh_them_giang_vien(self)
        self.ManHinhSuaGiangVien = Man_hinh_sua_giang_vien(self)

        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.close()

    def Them(self):
        self.ManHinhThemGiangVien.DatMacDinh()
        self.ManHinhThemGiangVien.show()

    def Sua(self):
        giang_vien = self.danh_sach_giang_vien.currentRow()
        if giang_vien >= 0:
            ma_giang_vien = int(self.danh_sach_giang_vien.item(giang_vien, 0).text())
            self.ManHinhSuaGiangVien.DatMacDinh(ma_giang_vien)
            self.ManHinhSuaGiangVien.show()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn độ khó cần sửa")
            msg.show()

    def DatMacDinh(self):
        self.danh_sach_giang_vien.setColumnCount(5)
        self.danh_sach_giang_vien.setHorizontalHeaderLabels(["Mã giảng viên","Tên giảng viên", "Gmail", "Mật khẩu", "Tình trạng"])
        self.danh_sach_giang_vien.setColumnWidth(0, 100)
        self.danh_sach_giang_vien.setColumnWidth(1, 200)
        self.danh_sach_giang_vien.setColumnWidth(2, 130)
        self.danh_sach_giang_vien.setColumnWidth(3, 130)
        self.danh_sach_giang_vien.setColumnWidth(4, 80)
        
        self.danh_sach_giang_vien.clearContents()
        self.danh_sach_giang_vien.setRowCount(0)

        # Lấy danh sách năm học
        command = """select MaGiangVien, TenGiangVien, Gmail, MatKhau, TinhTrang
                    from GIANGVIEN"""
        result = self.mycursor.execute(command)

        for row_number, row_data in enumerate(result):
            self.danh_sach_giang_vien.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_giang_vien.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))