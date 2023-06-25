from window.danh_sach_ket_qua_cham_thi.ui_man_hinh_danh_sach_ket_qua_cham_thi import Ui_man_hinh_danh_sach_ket_qua_cham_thi
from PyQt6 import QtWidgets

class Man_hinh_danh_sach_ket_qua_cham_thi(QtWidgets.QWidget, Ui_man_hinh_danh_sach_ket_qua_cham_thi):
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
        self.par.switch_ManHinhLapKetQuaChamThi()

    def Xoa(self):
        kq_cham_thi = self.danh_sach_ket_qua_cham_thi.currentRow()
        if kq_cham_thi >= 0:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Bạn có chắc chắn muốn xóa kết quả chấm thi này không?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)
            button_clicked = msg.exec()
            if button_clicked == QtWidgets.QMessageBox.StandardButton.Ok:
                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle("Thông báo")
                try:
                    ma_kq_cham_thi = int(self.danh_sach_ket_qua_cham_thi.item(kq_cham_thi, 0).text())

                    # Xóa các chi tiết kết quả chấm thi
                    command = f"""delete from CT_KETQUACHAMTHI where MaKQChamThi = {ma_kq_cham_thi}"""
                    self.mycursor.execute(command)
                    self.mycursor.commit()

                    # Xóa kết quả chấm thi
                    command = f"""delete from KETQUACHAMTHI where MaKQChamThi = {ma_kq_cham_thi}"""
                    self.mycursor.execute(command)
                    self.mycursor.commit()

                    self.danh_sach_ket_qua_cham_thi.removeRow(kq_cham_thi)
                    msg.setInformativeText("Xóa kết quả chấm thi thành công")
                except:
                    msg.setInformativeText("Xóa thất bại. Kết quả chấm thi này đã được báo cáo vào các năm trước.")
                msg.show()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn kết quả chấm thi cần xóa cần xóa")
            msg.show()

    def Sua(self):
        ket_qua_cham_thi = self.danh_sach_ket_qua_cham_thi.currentRow()
        if ket_qua_cham_thi >= 0:
            ket_qua_cham_thi = int(self.danh_sach_ket_qua_cham_thi.item(ket_qua_cham_thi, 0).text())
            self.par.switch_ManHinhSuaKetQuaChamThi(ket_qua_cham_thi)
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn đề thi cần sửa")
            msg.show()

    def TimKiem(self):
        mon_hoc = self.mon_hoc.currentText()
        nam_hoc = self.nam_hoc.currentText()
        hoc_ky = self.hoc_ky.currentText()

        command = f"""select kq.MaKQChamThi, l.TenLop, d.MaDeThi, d.TieuDe, kq.TongSoBaiCham
                    from KETQUACHAMTHI kq, DETHI d, MONHOC m, NAMHOC n, HOCKY h, LOPHOC l
                    where kq.MaDeThi = d.MaDeThi
                    and kq.MaLop = l.MaLop
                    and d.MaMonHoc = m.MaMonHoc
                    and d.MaNamHoc = n.MaNamHoc
                    and d.MaHocKy = h.MaHocKy
                    and n.TenNamHoc = N'{nam_hoc}'
                    and h.TenHocKy = N'{hoc_ky}'
                    and m.TenMonHoc = N'{mon_hoc}' """
        
        result = self.mycursor.execute(command).fetchall()

        self.danh_sach_ket_qua_cham_thi.clearContents()
        self.danh_sach_ket_qua_cham_thi.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.danh_sach_ket_qua_cham_thi.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.danh_sach_ket_qua_cham_thi.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


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
        self.danh_sach_ket_qua_cham_thi.setColumnCount(5)
        self.danh_sach_ket_qua_cham_thi.setHorizontalHeaderLabels(["Mã bài chấm","Lớp học", "Mã đề", "Tiêu đề", "Tổng số bài chấm"])
        self.danh_sach_ket_qua_cham_thi.setColumnWidth(0, 100)
        self.danh_sach_ket_qua_cham_thi.setColumnWidth(1, 80)
        self.danh_sach_ket_qua_cham_thi.setColumnWidth(2, 80)
        self.danh_sach_ket_qua_cham_thi.setColumnWidth(3, 270)
        self.danh_sach_ket_qua_cham_thi.setColumnWidth(4, 130)

        self.danh_sach_ket_qua_cham_thi.clearContents()
        self.danh_sach_ket_qua_cham_thi.setRowCount(0)