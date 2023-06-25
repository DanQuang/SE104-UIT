from admin.ui_man_hinh_bang_do_kho import Ui_man_hinh_bang_do_kho
from admin.man_hinh_them_do_kho import Man_hinh_them_do_kho
from admin.man_hinh_sua_do_kho import Man_hinh_sua_do_kho
from PyQt6 import QtWidgets

class Man_hinh_bang_do_kho(QtWidgets.QWidget, Ui_man_hinh_bang_do_kho):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.conn.cursor()
        self.setFixedSize(960, 540)

        self.ManHinhThemDoKho = Man_hinh_them_do_kho(self)
        self.ManHinhSuaDoKho = Man_hinh_sua_do_kho(self)

        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.close()

    def Them(self):
        self.ManHinhThemDoKho.DatMacDinh()
        self.ManHinhThemDoKho.show()

    def Sua(self):
        do_kho = self.danh_sach_do_kho.currentRow()
        if do_kho >= 0:
            ma_do_kho = int(self.danh_sach_do_kho.item(do_kho, 0).text())
            self.ManHinhSuaDoKho.DatMacDinh(ma_do_kho)
            self.ManHinhSuaDoKho.show()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn độ khó cần sửa")
            msg.show()

    def DatMacDinh(self):
        self.danh_sach_do_kho.setColumnCount(2)
        self.danh_sach_do_kho.setHorizontalHeaderLabels(["Mã độ khó","Tên độ khó"])
        self.danh_sach_do_kho.setColumnWidth(0, 300)
        self.danh_sach_do_kho.setColumnWidth(1, 350)
        
        self.danh_sach_do_kho.clearContents()
        self.danh_sach_do_kho.setRowCount(0)

        # Lấy danh sách năm học
        command = """select MaDoKho, TenDoKho
                    from DOKHO"""
        result = self.mycursor.execute(command)

        for row_number, row_data in enumerate(result):
            self.danh_sach_do_kho.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_do_kho.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))