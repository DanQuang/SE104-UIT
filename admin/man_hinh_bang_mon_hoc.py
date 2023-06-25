from admin.ui_man_hinh_bang_mon_hoc import Ui_man_hinh_bang_mon_hoc
from admin.man_hinh_them_mon_hoc import Man_hinh_them_mon_hoc
from admin.man_hinh_sua_mon_hoc import Man_hinh_sua_mon_hoc
from PyQt6 import QtWidgets

class Man_hinh_bang_mon_hoc(QtWidgets.QWidget, Ui_man_hinh_bang_mon_hoc):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.conn.cursor()
        self.setFixedSize(960, 540)

        self.ManHinhThemMonHoc = Man_hinh_them_mon_hoc(self)
        self.ManHinhSuaMonHoc = Man_hinh_sua_mon_hoc(self)

        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.close()

    def Them(self):
        self.ManHinhThemMonHoc.DatMacDinh()
        self.ManHinhThemMonHoc.show()

    def Sua(self):
        mon_hoc = self.danh_sach_mon.currentRow()
        if mon_hoc >= 0:
            ma_mon_hoc = int(self.danh_sach_mon.item(mon_hoc, 0).text())
            self.ManHinhSuaMonHoc.DatMacDinh(ma_mon_hoc)
            self.ManHinhSuaMonHoc.show()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn độ khó cần sửa")
            msg.show()

    def DatMacDinh(self):
        self.danh_sach_mon.setColumnCount(2)
        self.danh_sach_mon.setHorizontalHeaderLabels(["Mã môn học","Tên môn học"])
        self.danh_sach_mon.setColumnWidth(0, 300)
        self.danh_sach_mon.setColumnWidth(1, 350)
        
        self.danh_sach_mon.clearContents()
        self.danh_sach_mon.setRowCount(0)

        # Lấy danh sách năm học
        command = """select MaMonHoc, TenMonHoc
                    from MONHOC"""
        result = self.mycursor.execute(command)

        for row_number, row_data in enumerate(result):
            self.danh_sach_mon.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_mon.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))