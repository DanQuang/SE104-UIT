from window.danh_sach_de_thi.ui_man_hinh_danh_sach_de_thi import Ui_man_hinh_danh_sach_de_thi
from PyQt6 import QtWidgets

class Man_hinh_danh_sach_de_thi(QtWidgets.QWidget, Ui_man_hinh_danh_sach_de_thi):
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
        self.par.switch_ManHinhSoanDeThi()

    def Xoa(self):
        de_thi = self.danh_sach_de_thi.currentRow()
        if de_thi >= 0:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Bạn có chắc chắn muốn xóa đề thi này không?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)
            button_clicked = msg.exec()
            if button_clicked == QtWidgets.QMessageBox.StandardButton.Ok:
                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle("Thông báo")
                try:
                    ma_de_thi = int(self.danh_sach_de_thi.item(de_thi, 0).text())

                    # Xóa các chi tiết đề thi
                    command = f"""delete from CT_DETHI where MaDeThi = {ma_de_thi}"""
                    self.mycursor.execute(command)
                    self.mycursor.commit()

                    # Xóa đề thi
                    command = f"""delete from DETHI where MaDeThi = {ma_de_thi}"""
                    self.mycursor.execute(command)
                    self.mycursor.commit()

                    self.danh_sach_de_thi.removeRow(de_thi)
                    msg.setInformativeText("Xóa đề thi thành công")
                except:
                    msg.setInformativeText("Xóa đề thi thất bại. Đề thi này đã được chấm.")
                msg.show()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn đề thi cần xóa")
            msg.show()

    def Sua(self):
        de_thi = self.danh_sach_de_thi.currentRow()
        if de_thi >= 0:
            ma_de_thi = int(self.danh_sach_de_thi.item(de_thi, 0).text())
            self.par.switch_ManHinhSuaDeThi(ma_de_thi)
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn đề thi cần sửa")
            msg.show()

    def TimKiem(self):
        self.danh_sach_de_thi.clearContents()
        self.danh_sach_de_thi.setRowCount(0)

        mon_hoc = self.mon_hoc.currentText()
        nam_hoc = self.nam_hoc.currentText()
        hoc_ky = self.hoc_ky.currentText()

        command = f"""select d.MaDeThi, d.ThoiLuong, d.NgayThi
                    from DETHI d, MONHOC m, NAMHOC n, HOCKY h
                    where d.MaMonHoc = m.MaMonHoc
                    and d.MaNamHoc = n.MaNamHoc
                    and d.MaHocKy = h.MaHocKy
                    and n.TenNamHoc = N'{nam_hoc}'
                    and h.TenHocKy = N'{hoc_ky}'
                    and m.TenMonHoc = N'{mon_hoc}' """

        result = self.mycursor.execute(command).fetchall()

        for row_number, row_data in enumerate(result):
            self.danh_sach_de_thi.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_de_thi.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def Thoat(self):
        self.par.par.switch_ManHinhChinh()

    def DatMacDinh(self):
        # Xóa toàn bộ combobox trước
        self.mon_hoc.clear()
        self.nam_hoc.clear()
        self.hoc_ky.clear()

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

        # Thêm giá trị vào combobox năm học
        command = """select TenNamHoc
                    from NAMHOC"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.nam_hoc.addItem(row[0])

        # Thêm giá trị vào combobox học kỳ
        command = """select TenHocKy
                    from HOCKY"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.hoc_ky.addItem(row[0])

        # Đặt chính sách kích thước cho MyWidget
        self.setFixedSize(960, 540)
        self.danh_sach_de_thi.setColumnCount(3)
        self.danh_sach_de_thi.setHorizontalHeaderLabels(["Mã số đề thi", "Thời lượng", "Ngày thi"])
        self.danh_sach_de_thi.setColumnWidth(0, 100)
        self.danh_sach_de_thi.setColumnWidth(1, 100)
        self.danh_sach_de_thi.setColumnWidth(2, 450)

        self.danh_sach_de_thi.clearContents()
        self.danh_sach_de_thi.setRowCount(0)