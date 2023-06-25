from PyQt6 import QtWidgets
from window.danh_sach_ket_qua_cham_thi.ui_man_hinh_sua_ket_qua_cham_thi import Ui_man_hinh_sua_ket_qua_cham_thi

class Man_hinh_sua_ket_qua_cham_thi(QtWidgets.QWidget, Ui_man_hinh_sua_ket_qua_cham_thi):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mycursor = self.par.par.par.conn.cursor()

        # Thêm giá trị vào combobox lớp học
        command = """select TenLop
                    from LOPHOC"""
        result = self.mycursor.execute(command).fetchall()
        for row in result:
            self.lop_hoc.addItem(row[0])

        # Thêm môn học
        command = """select TenMonHoc
                    from MONHOC"""
        result = self.mycursor.execute(command).fetchall()
        for row in result:
            self.mon_hoc.addItem(row[0])

        # Thêm Mã đề
        command = """select MaDeThi
                    from DETHI"""
        result = self.mycursor.execute(command).fetchall()
        for row in result:
            self.ma_de.addItem(str(row[0]))


        # Các yếu tố không được sửa trong 
        self.ma_ket_qua_cham_thi = None
        self.ma_lop_hoc = None
        self.ma_mon_hoc = None
        self.ma_de_thi = None
        self.giang_vien = None

        
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.par.switch_ManHinhDanhSachKetQuaChamThi()

    def Sua(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")

        diemso_filled = self.ket_qua_cham_thi.rowCount() > 0 and all(self.ket_qua_cham_thi.item(row, 2) is not None or not '' for row in range(self.ket_qua_cham_thi.rowCount()))
        diemchu_filled = self.ket_qua_cham_thi.rowCount() > 0 and all(self.ket_qua_cham_thi.item(row, 3) is not None or not '' for row in range(self.ket_qua_cham_thi.rowCount()))
        
        if (diemso_filled):
            if (diemchu_filled):
                # Tổng số bài chấm 
                tong_so_bai_cham = 0
                for row in range(self.ket_qua_cham_thi.rowCount()):
                    item = self.ket_qua_cham_thi.item(row, 4)
                    if item is None or item.text().lower() != "vắng":       
                        tong_so_bai_cham += 1

                # Xóa các chi tiết kết quả chấm thi cũ
                command = f"""delete from CT_KETQUACHAMTHI
                                    where MaKQChamThi = {self.ma_ket_qua_cham_thi}"""
                        
                self.mycursor.execute(command)
                self.mycursor.commit()

                # Thêm chi tiết kết quả chấm thi mới

                # Thêm lần lượt các chi tiết kết quả chấm thi
                for row in range(self.ket_qua_cham_thi.rowCount()):
                    danh_sach_gia_tri = []
                    for col in range(self.ket_qua_cham_thi.columnCount()):
                        item = self.ket_qua_cham_thi.item(row, col)
                        if item == None:
                            item = "không"
                        danh_sach_gia_tri.append(item.text())
                    
                    mssv = int(danh_sach_gia_tri[0])
                    diem_so = float(danh_sach_gia_tri[2])
                    diem_chu = danh_sach_gia_tri[3]
                    ghi_chu = danh_sach_gia_tri[-1]

                    command = f"""insert into CT_KETQUACHAMTHI
                                values ({self.ma_ket_qua_cham_thi}, {mssv}, {diem_so}, N'{diem_chu}', N'{ghi_chu}')"""
                    
                    self.mycursor.execute(command)
                    self.mycursor.commit()
                
                # Sửa lại tổng số bài chấm
                command = f"""update KETQUACHAMTHI
                            set TongSoBaiCham = {tong_so_bai_cham} 
                            where MaKQChamThi = {self.ma_ket_qua_cham_thi}"""
                self.mycursor.execute(command)
                self.mycursor.commit()

                # Thông báo
                msg.setInformativeText("Sửa thành công.")
            else:
                msg.setInformativeText("Vui lòng nhập đủ điểm chữ cho sinh viên")
        else:
            msg.setInformativeText("Vui lòng nhập đủ điểm số cho sinh viên")
        msg.show()

    def DatMacDinh(self, ma_ket_qua_cham_thi):
        self.setFixedSize(960, 540)

        # Lấy mã kết quả chấm thi cần sửa
        self.ma_ket_qua_cham_thi = ma_ket_qua_cham_thi

        # Lấy các thông tin của kết quả chấm thi ra
        command = f"""select kq.MaLop,d.MaMonHoc, kq.MaDeThi, g.TenGiangVien
                    from KETQUACHAMTHI kq, DETHI d, GIANGVIEN g
                    where MaKQChamThi = {self.ma_ket_qua_cham_thi}
                    and kq.MaDeThi = d.MaDeThi
                    and kq.MaGiangVien = g.MaGiangVien"""
        result = self.mycursor.execute(command).fetchall()
        # print(result)
        # Lấy ra các yếu tố để hiển thị
        self.ma_lop_hoc = int(result[0][0])
        self.ma_mon_hoc = int(result[0][1])
        self.ma_de_thi = int(result[0][2])
        self.giang_vien = str(result[0][3])

        # Lấy ra tên môn học
        command = f"""select TenMonHoc
                    from MONHOC
                    where MaMonHoc = {self.ma_mon_hoc}"""
        ten_mon_hoc = self.mycursor.execute(command).fetchall()[0][0]

        # Lấy ra tên lớp học
        command = f"""select TenLop
                    from LOPHOC
                    where MaLop = {self.ma_lop_hoc}"""
        ten_lop_hoc = self.mycursor.execute(command).fetchall()[0][0]


        self.lop_hoc.setCurrentText(f"{ten_lop_hoc}")
        self.mon_hoc.setCurrentText(f"{ten_mon_hoc}")
        self.ma_de.setCurrentText(f"{self.ma_de_thi}")
        self.ten_giang_vien.setText(self.giang_vien)

        # Không cho người dùng thay đổi 4 yếu tố trên
        self.lop_hoc.setEnabled(False)
        self.mon_hoc.setEnabled(False)
        self.ma_de.setEnabled(False)
        self.ten_giang_vien.setEnabled(False)

        # Lấy ra các chi tiết kết quả để hiển thị
        # Thiết lập bảng
        self.ket_qua_cham_thi.setColumnCount(5)
        self.ket_qua_cham_thi.setColumnCount(5)
        self.ket_qua_cham_thi.setHorizontalHeaderLabels(["Mã số sinh viên", "Họ tên", "Điểm số", "Điểm chữ", "Ghi chú"])
        self.ket_qua_cham_thi.setColumnWidth(0, 100)
        self.ket_qua_cham_thi.setColumnWidth(1, 200)
        self.ket_qua_cham_thi.setColumnWidth(2, 100)
        self.ket_qua_cham_thi.setColumnWidth(2, 100)
        self.ket_qua_cham_thi.setColumnWidth(2, 150)

        self.ket_qua_cham_thi.clearContents()
        self.ket_qua_cham_thi.setRowCount(0)
        
        # Lấy ra các chi tiết kết quả từ server
        command = f"""select ct.MSSV, sv.TenSinhVien, ct.DiemSo, ct.DiemChu, ct.GhiChu
                    from CT_KETQUACHAMTHI ct, SINHVIEN sv
                    where ct.MaKQChamThi = {self.ma_ket_qua_cham_thi}
                    and ct.MSSV = sv.MSSV"""
        result = self.mycursor.execute(command).fetchall()
        
        for row_number, row_data in enumerate(result):
            self.ket_qua_cham_thi.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.ket_qua_cham_thi.setItem(row_number, column_number, item)
