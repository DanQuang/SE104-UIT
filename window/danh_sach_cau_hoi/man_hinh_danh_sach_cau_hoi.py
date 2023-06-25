from window.danh_sach_cau_hoi.ui_man_hinh_danh_sach_cau_hoi import Ui_man_hinh_danh_sach_cau_hoi
from PyQt6 import QtWidgets

class Man_hinh_danh_sach_cau_hoi(QtWidgets.QWidget, Ui_man_hinh_danh_sach_cau_hoi):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mycursor = self.par.par.par.conn.cursor()
        self.DatMacDinh()

        # Chức năng các nút
        self.them.clicked.connect(self.Them)
        self.xoa.clicked.connect(self.Xoa)
        self.sua.clicked.connect(self.Sua)
        self.tim_kiem.clicked.connect(self.TimKiem)
        self.thoat.clicked.connect(self.Thoat)

    def Them(self):
        self.par.switch_ManHinhSoanCauHoi()

    def Xoa(self):
        cau_hoi = self.danh_sach_cau_hoi.currentRow()
        if cau_hoi >= 0:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Bạn có chắc chắn muốn xóa câu hỏi này không?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)
            button_clicked = msg.exec()
            if button_clicked == QtWidgets.QMessageBox.StandardButton.Ok:
                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle("Thông báo")
                try:
                    ma_cau_hoi = int(self.danh_sach_cau_hoi.item(cau_hoi, 0).text())

                    command = f"""delete from CAUHOI where MaCauHoi = {ma_cau_hoi}"""
                    self.mycursor.execute(command)
                    self.mycursor.commit()

                    self.danh_sach_cau_hoi.removeRow(cau_hoi)
                    msg.setInformativeText("Xóa câu hỏi thành công")
                except:
                    msg.setInformativeText("Xóa câu hỏi thất bại. Câu hỏi này nằm trong 1 đề thi")
            msg.show()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn câu hỏi cần xóa")
            msg.show()

    def Sua(self):
        cau_hoi = self.danh_sach_cau_hoi.currentRow()
        if cau_hoi >= 0:
            ma_cau_hoi = int(self.danh_sach_cau_hoi.item(cau_hoi, 0).text())
            self.par.switch_ManHinhSuaCauHoi(ma_cau_hoi)
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn câu hỏi cần sửa")
            msg.show()

    def TimKiem(self):
        self.danh_sach_cau_hoi.clearContents()
        self.danh_sach_cau_hoi.setRowCount(0)
        
        mon_hoc = self.mon_hoc.currentText()
        do_kho = self.do_kho.currentText()

        command = f"""select c.MaCauHoi, m.TenMonHoc, d.TenDoKho, c.NoiDungCauHoi
                    from CAUHOI c, DOKHO d, MONHOC m
                    where c.MaDoKho = d.MaDoKho
                    and c.MaMonHoc = m.MaMonHoc
                    and m.TenMonHoc = N'{mon_hoc}'
                    and d.TenDoKho = N'{do_kho}' """

        result = self.mycursor.execute(command).fetchall()

        for row_number, row_data in enumerate(result):
            self.danh_sach_cau_hoi.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_cau_hoi.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def Thoat(self):
        self.par.par.switch_ManHinhChinh()

    def DatMacDinh(self):

        self.mon_hoc.clear()
        self.do_kho.clear()

        self.MaGiangVien = self.par.par.par.MaGiangVien
        # Thêm giá trị vào combobox môn học
        command = f"""select TenMonHoc
                    from GIANGVIEN g, CT_GIANGVIEN ct, MONHOC m
                    where g.MaGiangVien = ct.MaGiangVien
                    and ct.MaMonHoc = m.MaMonHoc
                    and g.MaGiangVien = {self.MaGiangVien}"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.mon_hoc.addItem(row[0])

        # Thêm giá trị vào combobox độ khó
        command = """select TenDoKho
                    from DOKHO"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.do_kho.addItem(row[0])
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