from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from window.danh_sach_de_thi.ui_man_hinh_them_cau_hoi import Ui_man_hinh_them_cau_hoi

class Man_hinh_them_cau_hoi(QtWidgets.QDialog, Ui_man_hinh_them_cau_hoi):
    def __init__(self, parent= None, mon_hoc = None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mon_hoc = mon_hoc
        self.mycursor = self.par.par.par.par.conn.cursor()
        self.DatMacDinh()
        self.cau_hoi = []

        command = """select TenDoKho
                    from DOKHO"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.do_kho.addItem(row[0])

        self.tim_kiem.clicked.connect(self.TimKiem)
        self.them.clicked.connect(self.Them)
        self.danh_sach_cau_hoi.itemSelectionChanged.connect(self.ChonCauHoi)
        self.thoat.clicked.connect(self.Thoat)

    def Thoat(self):
        self.close()

    def TimKiem(self):
        self.danh_sach_cau_hoi.clearContents()
        self.danh_sach_cau_hoi.setRowCount(0)

        do_kho = self.do_kho.currentText()

        command = f"""select c.MaCauHoi, m.TenMonHoc, d.TenDoKho, c.NoiDungCauHoi
                    from CAUHOI c, DOKHO d, MONHOC m
                    where c.MaDoKho = d.MaDoKho
                    and c.MaMonHoc = m.MaMonHoc
                    and m.TenMonHoc = N'{self.mon_hoc}'
                    and d.TenDoKho = N'{do_kho}' """

        result = self.mycursor.execute(command).fetchall()

        for row_number, row_data in enumerate(result):
            self.danh_sach_cau_hoi.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_cau_hoi.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def ChonCauHoi(self):
        self.cau_hoi = [item.text() for item in self.danh_sach_cau_hoi.selectedItems()]
        

    def Them(self):
        try:
            diem = float(self.diem.text())
            if (self.cau_hoi != []) and diem > 0 and diem <= 10:
                row = self.par.danh_sach_cau_hoi.rowCount()
                self.par.danh_sach_cau_hoi.insertRow(row)

                for col, data in enumerate(self.cau_hoi):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                    self.par.danh_sach_cau_hoi.setItem(row, col, item)
                
                # Thêm điểm vào cuối
                col = self.par.danh_sach_cau_hoi.columnCount() - 1
                item = QtWidgets.QTableWidgetItem(str(diem))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.par.danh_sach_cau_hoi.setItem(row, col, item)
                
                # Chỉnh lại số câu ở soạn đề thi
                so_cau = int(self.par.so_cau.text()) + 1
                self.par.so_cau.setText(str(so_cau))

                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle("Thông báo")
                msg.setInformativeText("Thêm thành công")
                msg.show()
            else:
                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle("Thông báo")
                msg.setInformativeText("Điểm câu hỏi phải nằm trong khoảng quy định")
                msg.show()
        except:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng nhập điểm thích hợp")
            msg.show()
    

    def DatMacDinh(self):
        # Đặt chính sách kích thước cho MyWidget, thêm tên cột cho danh sách câu hỏi
        self.setFixedSize(960, 540)
        self.danh_sach_cau_hoi.setColumnCount(4)
        self.danh_sach_cau_hoi.setHorizontalHeaderLabels(["Mã câu hỏi","Môn học", "Độ khó", "Nội dung câu hỏi"])
        self.danh_sach_cau_hoi.setColumnWidth(0, 100)
        self.danh_sach_cau_hoi.setColumnWidth(1, 100)
        self.danh_sach_cau_hoi.setColumnWidth(2, 100)
        self.danh_sach_cau_hoi.setColumnWidth(3, 350)
        
        self.danh_sach_cau_hoi.clearContents()
        self.danh_sach_cau_hoi.setRowCount(0)