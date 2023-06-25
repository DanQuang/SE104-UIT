from PyQt6 import QtWidgets
from window.danh_sach_de_thi.ui_man_hinh_soan_de_thi import Ui_man_hinh_soan_de_thi
from window.danh_sach_de_thi.man_hinh_them_cau_hoi import Man_hinh_them_cau_hoi

class Man_hinh_soan_de_thi(QtWidgets.QWidget, Ui_man_hinh_soan_de_thi):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mycursor = self.par.par.par.conn.cursor()
        self.MaGiangVien = self.par.par.par.MaGiangVien
        self.DatMacDinh()
        
        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)
        self.them_cau_hoi.clicked.connect(self.ThemCauHoi)
        self.xoa_cau_hoi.clicked.connect(self.XoaCauHoi)

    def Thoat(self):
        self.par.switch_ManHinhDanhSachDeThi()

    def ThemCauHoi(self):
        mon_hoc = self.mon_hoc.currentText()
        them_cau_hoi = Man_hinh_them_cau_hoi(self, mon_hoc)
        them_cau_hoi.show()

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


        self.setFixedSize(960, 540)
        self.danh_sach_cau_hoi.setColumnCount(5)
        self.danh_sach_cau_hoi.setHorizontalHeaderLabels(["Mã câu hỏi","Môn học", "Độ khó", "Nội dung câu hỏi", "Điểm"])
        self.danh_sach_cau_hoi.setColumnWidth(0, 80)
        self.danh_sach_cau_hoi.setColumnWidth(1, 80)
        self.danh_sach_cau_hoi.setColumnWidth(2, 80)
        self.danh_sach_cau_hoi.setColumnWidth(3, 350)
        self.danh_sach_cau_hoi.setColumnWidth(4, 80)
        
        self.danh_sach_cau_hoi.clearContents()
        self.danh_sach_cau_hoi.setRowCount(0)
        self.so_cau.setText('0')

    def XoaCauHoi(self):
        cau_hoi = self.danh_sach_cau_hoi.currentRow()
        if cau_hoi >= 0:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Bạn có chắc chắn muốn xóa câu hỏi này không?")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)
            button_clicked = msg.exec()
            if button_clicked == QtWidgets.QMessageBox.StandardButton.Ok:
                self.danh_sach_cau_hoi.removeRow(cau_hoi)
                so_cau = int(self.so_cau.text()) - 1
                self.so_cau.setText(str(so_cau))
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Thông báo")
            msg.setInformativeText("Vui lòng chọn câu cần xóa")
            msg.show()

    def Them(self):
        # Tạo một thông báo
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")

        if (self.danh_sach_cau_hoi.rowCount() > 0):
            if (self.thoi_luong.text().isdigit() and (int(self.thoi_luong.text()) >= 30) and (int(self.thoi_luong.text()) <= 180)):
                if (self.tieu_de.text() != ''):
                    column_index = 4
                    tong_diem = 0
                    for row in range(self.danh_sach_cau_hoi.rowCount()):
                        diem = self.danh_sach_cau_hoi.item(row, column_index)
                        tong_diem += float(diem.text())
                    if tong_diem != 10:
                        msg.setInformativeText("Tổng điểm phải bằng 10.")
                    else:
                        # Thêm đề mới vào
                        mon_hoc = self.mon_hoc.currentText()
                        hoc_ky = self.hoc_ky.currentText()
                        nam_hoc = self.nam_hoc.currentText()
                        ngay_thi = self.ngay_thi.text()
                        thoi_luong = int(self.thoi_luong.text())
                        tieu_de = self.tieu_de.text()
                        so_cau = int(self.so_cau.text())

                        #Lấy mã môn học, mã năm học và mã học kỳ 
                        command = f"""select MaMonHoc
                                    from MONHOC
                                    where MONHOC.TenMonHoc = N'{mon_hoc}' """
                        ma_mon_hoc = int(self.mycursor.execute(command).fetchall()[0][0])

                        command = f"""select MaNamHoc
                                    from NAMHOC
                                    where NAMHOC.TenNamHoc = N'{nam_hoc}' """
                        ma_nam_hoc = int(self.mycursor.execute(command).fetchall()[0][0])

                        command = f"""select MaHocKy
                                    from HOCKY
                                    where HOCKY.TenHocKy = N'{hoc_ky}' """
                        ma_hoc_ky = int(self.mycursor.execute(command).fetchall()[0][0])

                        command = f"""INSERT INTO DETHI
                                    VALUES ({self.MaGiangVien}, {ma_hoc_ky}, {ma_nam_hoc}, {ma_mon_hoc}, {thoi_luong}, N'{tieu_de}', '{ngay_thi}', {so_cau})"""
                        
                        self.mycursor.execute(command)
                        self.mycursor.commit()

                        # Thêm các chi tiết đề thi
                        #Lấy ra mã đề mới nhất
                        command = """select MAX(MaDeThi)
                                    from DETHI"""
                        ma_de_thi = int(self.mycursor.execute(command).fetchall()[0][0])

                        # Thêm lần lượt các chi tiết đề thi
                        for row in range(self.danh_sach_cau_hoi.rowCount()):
                            danh_sach_gia_tri = []
                            for col in range(self.danh_sach_cau_hoi.columnCount()):
                                item = self.danh_sach_cau_hoi.item(row, col)
                                danh_sach_gia_tri.append(item.text())
                            
                            ma_cau_hoi = int(danh_sach_gia_tri[0])
                            diem = float(danh_sach_gia_tri[-1])

                            command = f"""insert into CT_DETHI
                                        values ({ma_de_thi}, {ma_cau_hoi}, {diem})"""
                            
                            self.mycursor.execute(command)
                            self.mycursor.commit()

                        # Thông báo
                        msg.setInformativeText("Thêm thành công.")
                else:
                    msg.setInformativeText("Bạn chưa thêm tiêu đề")
            else:
                msg.setInformativeText("Vui lòng nhập thời lượng phù hợp")

        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setInformativeText("Chưa có câu hỏi trong đề.")

        msg.show()
