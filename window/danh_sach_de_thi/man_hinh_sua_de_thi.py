from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QDate
from window.danh_sach_de_thi.ui_man_hinh_sua_de_thi import Ui_man_hinh_sua_de_thi
from window.danh_sach_de_thi.man_hinh_them_cau_hoi import Man_hinh_them_cau_hoi

class Man_hinh_sua_de_thi(QtWidgets.QWidget, Ui_man_hinh_sua_de_thi):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mycursor = self.par.par.par.conn.cursor()

        # Các yếu tố không được sửa trong đề
        self.ma_de_thi = None
        self.ma_mon_hoc = None
        self.ma_nam_hoc = None
        self.ma_hoc_ky = None

        # Thêm giá trị vào combobox môn học
        command = """select TenMonHoc
                    from MONHOC"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.mon_hoc.addItem(row[0])
            self.mon_hoc.currentText
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

        
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)
        self.them_cau_hoi.clicked.connect(self.ThemCauHoi)
        self.xoa_cau_hoi.clicked.connect(self.XoaCauHoi)

    def Thoat(self):
        self.par.switch_ManHinhDanhSachDeThi()

    def ThemCauHoi(self):
        mon_hoc = self.mon_hoc.currentText()
        them_cau_hoi = Man_hinh_them_cau_hoi(self, mon_hoc)
        them_cau_hoi.show()

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

    def Sua(self):
        # Tạo một thông báo
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")

        if (self.danh_sach_cau_hoi.rowCount() > 0):
            if (self.thoi_luong.text().isdigit()):
                if (self.tieu_de.text() != ''):
                    column_index = 4
                    tong_diem = 0
                    for row in range(self.danh_sach_cau_hoi.rowCount()):
                        diem = self.danh_sach_cau_hoi.item(row, column_index)
                        tong_diem += float(diem.text())
                    if tong_diem != 10:
                        msg.setInformativeText("Tổng điểm phải bằng 10.")
                    else:
                        # Xóa các CT_DETHI cũ đi
                        command = f"""delete from CT_DETHI
                                    where MaDeThi = {self.ma_de_thi}"""
                        
                        self.mycursor.execute(command)
                        self.mycursor.commit()

                        # Thêm lần lượt các chi tiết đề thi mới
                        for row in range(self.danh_sach_cau_hoi.rowCount()):
                            danh_sach_gia_tri = []
                            for col in range(self.danh_sach_cau_hoi.columnCount()):
                                item = self.danh_sach_cau_hoi.item(row, col)
                                danh_sach_gia_tri.append(item.text())
                            
                            ma_cau_hoi = int(danh_sach_gia_tri[0])
                            diem = float(danh_sach_gia_tri[-1])

                            command = f"""insert into CT_DETHI
                                        values ({self.ma_de_thi}, {ma_cau_hoi}, {diem})"""
                            
                            self.mycursor.execute(command)
                            self.mycursor.commit()

                        # Sửa các thông tin đề thi
                        ngay_thi = self.ngay_thi.text()
                        thoi_luong = int(self.thoi_luong.text())
                        tieu_de = self.tieu_de.text()
                        so_cau = int(self.so_cau.text())

                        command = f"""update DETHI
                                    set ThoiLuong = {thoi_luong}, TieuDe = N'{tieu_de}', NgayThi = '{ngay_thi}', SoCau = {so_cau} 
                                    where MaDeThi = {self.ma_de_thi}"""
                        self.mycursor.execute(command)
                        self.mycursor.commit()

                        # Thông báo
                        msg.setInformativeText("Sửa thành công.")
                else:
                    msg.setInformativeText("Bạn chưa thêm tiêu đề")
            else:
                msg.setInformativeText("Vui lòng nhập thời lượng phù hợp")
        else:
            msg.setInformativeText("Chưa có câu hỏi trong đề.")

        msg.show()

    def DatMacDinh(self, ma_de_thi):
        self.setFixedSize(960, 540)

        # Lấy mã đề thi cần sửa
        self.ma_de_thi = ma_de_thi

        # Lấy các thông tin của đề thi ra
        command = f"""select MaMonHoc, MaHocKy, MaNamHoc, ThoiLuong, TieuDe, NgayThi
                    from DETHI
                    where MaDeThi = {self.ma_de_thi}"""
        result = self.mycursor.execute(command).fetchall()

        # Lấy ra các yếu tố để hiển thị
        self.ma_mon_hoc = int(result[0][0])
        self.ma_hoc_ky = int(result[0][1])
        self.ma_nam_hoc = int(result[0][2])
        thoi_luong = str(result[0][3])
        tieu_de = result[0][4]
        ngay_thi = str(result[0][5])

        # Lấy ra tên môn học
        command = f"""select TenMonHoc
                    from MONHOC
                    where MaMonHoc = {self.ma_mon_hoc}"""
        ten_mon_hoc = self.mycursor.execute(command).fetchall()[0][0]

        # Lấy ra tên học kỳ
        command = f"""select TenHocKy
                    from HOCKY
                    where MaHocKy = {self.ma_hoc_ky}"""
        ten_hoc_ky = self.mycursor.execute(command).fetchall()[0][0]

        # Lấy ra tên năm học
        command = f"""select TenNamHoc
                    from NAMHOC
                    where MaNamHoc = {self.ma_nam_hoc}"""
        ten_nam_hoc = self.mycursor.execute(command).fetchall()[0][0]

        self.mon_hoc.setCurrentText(f"{ten_mon_hoc}")
        self.hoc_ky.setCurrentText(f"{ten_hoc_ky}")
        self.nam_hoc.setCurrentText(f"{ten_nam_hoc}")

        # Không cho người dùng thay đổi 3 yếu tố trên
        self.mon_hoc.setEnabled(False)
        self.hoc_ky.setEnabled(False)
        self.nam_hoc.setEnabled(False)

        # Hiển thị các thời lượng, tiêu đề, ngày thi
        self.thoi_luong.setText(thoi_luong)
        self.tieu_de.setText(tieu_de)
        
        # Xử lý ngày thi
        nam, thang, ngay = ngay_thi.split('-')
        nam = int(nam)
        thang = int(thang)
        ngay = int(ngay)
        date = QDate(nam, thang, ngay)
        self.ngay_thi.setDate(date)

        # Lấy ra các chi tiết đề thi để hiển thị
        # Thiết lập bảng
        self.danh_sach_cau_hoi.setColumnCount(5)
        self.danh_sach_cau_hoi.setHorizontalHeaderLabels(["Mã câu hỏi","Môn học", "Độ khó", "Nội dung câu hỏi", "Điểm"])
        self.danh_sach_cau_hoi.setColumnWidth(0, 80)
        self.danh_sach_cau_hoi.setColumnWidth(1, 80)
        self.danh_sach_cau_hoi.setColumnWidth(2, 80)
        self.danh_sach_cau_hoi.setColumnWidth(3, 350)
        self.danh_sach_cau_hoi.setColumnWidth(4, 80)
        
        self.danh_sach_cau_hoi.clearContents()
        self.danh_sach_cau_hoi.setRowCount(0)
        
        # Lấy ra các chi tiết đề thi từ server
        command = f"""select c.MaCauHoi, m.TenMonHoc, d.TenDoKho, c.NoiDungCauHoi, ctdt.Diem
                    from CT_DETHI ctdt, CAUHOI c, MONHOC m, DOKHO d
                    where ctdt.MaDeThi = {self.ma_de_thi}
                    and ctdt.MaCauHoi = c.MaCauHoi
                    and c.MaMonHoc = m.MaMonHoc
                    and c.MaDoKho = d.MaDoKho"""
        result = self.mycursor.execute(command).fetchall()

        for row_number, row_data in enumerate(result):
            self.danh_sach_cau_hoi.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.danh_sach_cau_hoi.setItem(row_number, column_number, item)

        # Hiển thị số câu
        self.so_cau.setText(str(self.danh_sach_cau_hoi.rowCount()))