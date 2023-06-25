from PyQt6 import QtWidgets
from window.danh_sach_ket_qua_cham_thi.ui_man_hinh_lap_ket_qua_cham_thi import Ui_man_hinh_lap_ket_qua_cham_thi

class Man_hinh_lap_ket_qua_cham_thi(QtWidgets.QWidget, Ui_man_hinh_lap_ket_qua_cham_thi):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mycursor = self.par.par.par.conn.cursor()
        self.DatMacDinh()

        # Thêm giá trị vào combobox lớp học
        command = """select TenLop
                    from LOPHOC"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.lop_hoc.addItem(row[0])
        
        # Trình tự chọn các combobox
        self.lop_hoc.currentTextChanged.connect(self.MonHoc)
        self.mon_hoc.currentTextChanged.connect(self.MaDe)

        self.tim_kiem.clicked.connect(self.TimKiem)
        self.them.clicked.connect(self.Them)
        self.thoat.clicked.connect(self.Thoat)

    def TimKiem(self):
        # self.DatMacDinh()
        self.ten_giang_vien.clear()
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")

        if (self.lop_hoc.currentIndex() != -1):
            lop_hoc = self.lop_hoc.currentText()
            mon_hoc = self.mon_hoc.currentText()
            ma_de = int(self.ma_de.currentText())

            command = f"""select count(kq.MaKQChamThi)
                        from KETQUACHAMTHI kq, LOPHOC l
                        where kq.MaDeThi = {ma_de}
                        and kq.MaLop = l.MaLop
                        and l.TenLop = N'{lop_hoc}' """
            
            result = int(self.mycursor.execute(command).fetchall()[0][0])
            if (result == 0):
                self.MaGiangVien = self.par.par.par.MaGiangVien
                command = f"""select TenGiangVien
                            from GIANGVIEN 
                            where  MaGiangVien = {self.MaGiangVien}"""
                
                ten_giang_vien = self.mycursor.execute(command).fetchall()[0][0]
                self.ten_giang_vien.setText(ten_giang_vien)

                command = f"""select sv.MSSV, sv.TenSinhVien
                            from LOPHOC l, CT_LOPHOC ctl, SINHVIEN sv
                            where l.MaLop = ctl.MaLop
                            and ctl.MSSV = sv.MSSV
                            and l.TenLop = N'{lop_hoc}' """
                
                result = self.mycursor.execute(command).fetchall()

                self.ket_qua_cham_thi.clearContents()
                self.ket_qua_cham_thi.setRowCount(0)

                for row_number, row_data in enumerate(result):
                    self.ket_qua_cham_thi.insertRow(row_number)

                    for column_number, data in enumerate(row_data):
                        self.ket_qua_cham_thi.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))           
                    self.ket_qua_cham_thi.setItem(row_number + 1, -1, QtWidgets.QTableWidgetItem("không"))
            else:
                msg.setInformativeText("Kết quả chấm thi của lớp này đã tồn tại")
                msg.show()
        else:
            msg.setInformativeText("Vui lòng chọn thông tin cần thiết")
            msg.show()

    def Them(self):

        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")

        diemso_filled = self.ket_qua_cham_thi.rowCount() > 0 and all(self.ket_qua_cham_thi.item(row, 2) is not None for row in range(self.ket_qua_cham_thi.rowCount()))
        diemchu_filled = self.ket_qua_cham_thi.rowCount() > 0 and all(self.ket_qua_cham_thi.item(row, 3) is not None for row in range(self.ket_qua_cham_thi.rowCount()))
        
        if (diemso_filled):
            if (diemchu_filled):
                # Thêm kết quả chấm thi mới
                # Mã đề thi
                ma_de_thi = int(self.ma_de.currentText())

                # Mã lớp
                ten_lop = self.lop_hoc.currentText()
                command = f"""select l.MaLop   
                            from LOPHOC l
                            where l.TenLop = N'{ten_lop}'"""
                ma_lop = int(self.mycursor.execute(command).fetchall()[0][0])
                
                ma_giang_vien = self.MaGiangVien

                # Tổng số bài chấm 
                tong_so_bai_cham = 0
                for row in range(self.ket_qua_cham_thi.rowCount()):
                    item = self.ket_qua_cham_thi.item(row, 4)
                    if item is None or item.text().lower() != "vắng":       
                        tong_so_bai_cham += 1
                
                # Thêm Kết quả chấm thi
                command = f"""insert into KETQUACHAMTHI
                            values ({ma_de_thi}, {ma_lop}, {ma_giang_vien}, {tong_so_bai_cham})"""
                self.mycursor.execute(command)
                self.mycursor.commit()

                # Thêm chi tiết kết quả chấm thi
                # Lấy ra mã kết quả chấm thi mới nhất
                command = """select MAX(MaKQChamThi)
                            from KETQUACHAMTHI"""
                ma_kq_cham_thi = int(self.mycursor.execute(command).fetchall()[0][0])

                # Thêm lần lượt các chi tiết kết quả chấm thi
                for row in range(self.ket_qua_cham_thi.rowCount()):
                    danh_sach_gia_tri = []
                    for col in range(self.ket_qua_cham_thi.columnCount()):
                        item = self.ket_qua_cham_thi.item(row, col)
                        if item == None:
                            item == "không"
                        danh_sach_gia_tri.append(item.text())
                    
                    mssv = int(danh_sach_gia_tri[0])
                    diem_so = float(danh_sach_gia_tri[2])
                    diem_chu = danh_sach_gia_tri[3]
                    ghi_chu = danh_sach_gia_tri[-1]

                    command = f"""insert into CT_KETQUACHAMTHI
                                values ({ma_kq_cham_thi}, {mssv}, {diem_so}, N'{diem_chu}', N'{ghi_chu}')"""
                    
                    self.mycursor.execute(command)
                    self.mycursor.commit()

                # Thông báo
                msg.setInformativeText("Thêm thành công.")
            else:
                msg.setInformativeText("Vui lòng nhập đủ điểm chữ cho sinh viên")
        else:
            msg.setInformativeText("Vui lòng nhập đủ điểm số cho sinh viên")
        msg.show()

    def Thoat(self):
        self.par.switch_ManHinhDanhSachKetQuaChamThi()

    def MonHoc(self):
        self.mon_hoc.clear()
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
    
    def MaDe(self):
        self.ma_de.clear()
        # Thêm giá trị vào combobox môn học
        command = f"""select d.MaDeThi
                    from DETHI d, MONHOC m
                    where d.MaMonHoc = m.MaMonHoc
                    and m.TenMonHoc = '{self.mon_hoc.currentText()}' """
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.ma_de.addItem(str(row[0]))

    def DatMacDinh(self):
        self.lop_hoc.setCurrentIndex(-1)
        self.mon_hoc.setCurrentIndex(-1)
        self.ma_de.setCurrentIndex(-1)
        self.ten_giang_vien.clear()
        # Đặt chính sách kích thước cho MyWidget
        self.setFixedSize(960, 540)
        self.ket_qua_cham_thi.setColumnCount(5)
        self.ket_qua_cham_thi.setHorizontalHeaderLabels(["Mã số sinh viên", "Họ tên", "Điểm số", "Điểm chữ", "Ghi chú"])
        self.ket_qua_cham_thi.setColumnWidth(0, 100)
        self.ket_qua_cham_thi.setColumnWidth(1, 200)
        self.ket_qua_cham_thi.setColumnWidth(2, 100)
        self.ket_qua_cham_thi.setColumnWidth(2, 100)
        self.ket_qua_cham_thi.setColumnWidth(2, 150)

        self.ket_qua_cham_thi.clearContents()
        self.ket_qua_cham_thi.setRowCount(0)