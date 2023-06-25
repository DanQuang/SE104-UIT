from admin.ui_man_hinh_bang_nam_hoc import Ui_man_hinh_bang_nam_hoc
from admin.man_hinh_them_nam_hoc import Man_hinh_them_nam_hoc
from admin.man_hinh_sua_nam_hoc import Man_hinh_sua_nam_hoc
from PyQt6 import QtWidgets

class Man_hinh_bang_nam_hoc(QtWidgets.QWidget, Ui_man_hinh_bang_nam_hoc):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.conn.cursor()
        self.setFixedSize(960, 540)

        self.ManHinhThemNamHoc = Man_hinh_them_nam_hoc(self)
        self.ManHinhSuaNamHoc = Man_hinh_sua_nam_hoc(self)
        
        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.close()

    def Them(self):
        self.ManHinhThemNamHoc.DatMacDinh()
        self.ManHinhThemNamHoc.show()

    def Sua(self):
        nam_hoc = self.danh_sach_nam.currentRow()
        if nam_hoc >= 0:
            ma_nam_hoc = int(self.danh_sach_nam.item(nam_hoc, 0).text())
            self.ManHinhSuaNamHoc.DatMacDinh(ma_nam_hoc)
            self.ManHinhSuaNamHoc.show()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn năm học cần sửa")
            msg.show()

    def DatMacDinh(self):
        self.danh_sach_nam.setColumnCount(2)
        self.danh_sach_nam.setHorizontalHeaderLabels(["Mã năm học","Tên năm học"])
        self.danh_sach_nam.setColumnWidth(0, 300)
        self.danh_sach_nam.setColumnWidth(1, 350)
        
        self.danh_sach_nam.clearContents()
        self.danh_sach_nam.setRowCount(0)

        # Lấy danh sách năm học
        command = """select MaNamHoc, TenNamHoc
                    from NAMHOC"""
        result = self.mycursor.execute(command)

        for row_number, row_data in enumerate(result):
            self.danh_sach_nam.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_nam.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))