from admin.ui_man_hinh_quan_ly_he_thong import Ui_man_hinh_quan_ly_he_thong
from admin.man_hinh_bang_admin import Man_hinh_bang_admin
from admin.man_hinh_bang_giang_vien import Man_hinh_bang_giang_vien
from admin.man_hinh_bang_mon_hoc import Man_hinh_bang_mon_hoc
from admin.man_hinh_bang_nam_hoc import Man_hinh_bang_nam_hoc
from admin.man_hinh_bang_do_kho import Man_hinh_bang_do_kho
from PyQt6 import QtWidgets

class Man_hinh_quan_ly_he_thong(QtWidgets.QWidget, Ui_man_hinh_quan_ly_he_thong):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.conn.cursor()
        self.setFixedSize(960, 540)

        self.BangAdmin = Man_hinh_bang_admin(self)
        self.BangGiangVien = Man_hinh_bang_giang_vien(self)
        self.BangMonHoc = Man_hinh_bang_mon_hoc(self)
        self.BangNamHoc = Man_hinh_bang_nam_hoc(self)
        self.BangDoKho = Man_hinh_bang_do_kho(self)

        self.nam_hoc.clicked.connect(self.NamHoc)
        self.do_kho.clicked.connect(self.DoKho)
        self.mon_hoc.clicked.connect(self.MonHoc)
        self.giang_vien.clicked.connect(self.GiangVien)
        self.admin.clicked.connect(self.Admin)
        self.thoat.clicked.connect(self.Thoat)
        self.thoat_2.clicked.connect(self.Thoat)
        self.cap_nhat.clicked.connect(self.CapNhap)

    def DatMacDinh(self):
        pass

    def NamHoc(self):
        self.BangNamHoc.DatMacDinh()
        self.BangNamHoc.show()

    def DoKho(self):
        self.BangDoKho.DatMacDinh()
        self.BangDoKho.show()

    def MonHoc(self):
        self.BangMonHoc.DatMacDinh()
        self.BangMonHoc.show()

    def GiangVien(self):
        self.BangGiangVien.DatMacDinh()
        self.BangGiangVien.show()

    def Admin(self):
        self.BangAdmin.DatMacDinh()
        self.BangAdmin.show()

    def Thoat(self):
        self.par.show_ManHinhDangNhap()

    def DatMacDinh(self):
        # Lấy ra các thông tin cần hiện
        command = """select GiaTri
                    from THAMSO"""
        
        result = self.mycursor.execute(command).fetchall()


        self.diem_so_cau_toi_da.setText(str(result[0][0]))
        self.diem_so_cau_toi_thieu.setText(str(result[1][0]))
        self.diem_so_toi_da.setText(str(result[2][0]))
        self.diem_so_toi_thieu.setText(str(result[3][0]))
        self.so_cau_toi_da.setText(str(result[4][0]))
        self.thoi_luong_toi_da.setText(str(result[5][0]))
        self.thoi_luong_toi_thieu.setText(str(result[6][0]))
        self.tong_diem_so.setText(str(result[7][0]))

    def CapNhap(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        msg.setFixedSize(400, 300)
        
        try:
            # Cập nhập  điểm số câu tối đa
            command = f"""update THAMSO
                        set GiaTri = {float(self.diem_so_cau_toi_da.text())}
                        where TenThamSo = N'DiemSoCauToiDa' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            # Cập nhập  điểm số câu tối thiểu
            command = f"""update THAMSO
                        set GiaTri = {float(self.diem_so_cau_toi_thieu.text())}
                        where TenThamSo = 'DiemSoCauToiThieu' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            # Cập nhập điểm số tối đa
            command = f"""update THAMSO
                        set GiaTri = {float(self.diem_so_toi_da.text())}
                        where TenThamSo = N'DiemSoToiDa' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            # Cập nhập  điểm số tối thiểu
            command = f"""update THAMSO
                        set GiaTri = {float(self.diem_so_toi_thieu.text())}
                        where TenThamSo = N'DiemSoToiThieu' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            # Cập nhập số câu tối đa
            command = f"""update THAMSO
                        set GiaTri = {float(self.so_cau_toi_da.text())}
                        where TenThamSo = N'SoCauToiDa' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            # Cập nhập thời lượng thi tối đa
            command = f"""update THAMSO
                        set GiaTri = {float(self.thoi_luong_toi_da.text())}
                        where TenThamSo = N'ThoiLuongThiToiDa' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            # Cập nhập thời lượng thi tối thiểu
            command = f"""update THAMSO
                        set GiaTri = {float(self.thoi_luong_toi_thieu.text())}
                        where TenThamSo = N'ThoiLuongThiToiThieu' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            # Cập nhập Tổng điểm
            command = f"""update THAMSO
                        set GiaTri = {float(self.tong_diem_so.text())}
                        where TenThamSo = N'TongDiem' """
            self.mycursor.execute(command)
            self.mycursor.commit()

            msg.setInformativeText("Cập nhập tham số thành công")
        except:
            msg.setInformativeText("Cập nhập tham số thất bại, vui lòng nhập đủ tham số và nhập dưới dạng số")
        msg.show()