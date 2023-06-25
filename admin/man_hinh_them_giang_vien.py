from admin.ui_man_hinh_them_giang_vien import Ui_man_hinh_them_giang_vien
from PyQt6 import QtWidgets

class Man_hinh_them_giang_vien(QtWidgets.QWidget, Ui_man_hinh_them_giang_vien):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.par.conn.cursor()
        self.setFixedSize(400, 300)
        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)

    def Thoat(self):
        self.par.DatMacDinh()
        self.close()

    def Them(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        if self.ten_giang_vien.text() != '':
            if self.ten_tai_khoan.text() != '':
                if self.mat_khau.text() != '':
                    if self.tinh_trang.text() != '' and self.tinh_trang.text().isnumeric():
                        ten_tai_khoan = self.ten_tai_khoan.text()
                        command = f"""select count(MaGiangVien)
                                    from GIANGVIEN
                                    where Gmail = N'{ten_tai_khoan}'"""
                        
                        result = int(self.mycursor.execute(command).fetchall()[0][0])
                        if result == 0:
                            command = f"""insert into GIANGVIEN values(N'{self.ten_giang_vien.text()}', N'{ten_tai_khoan}', N'{self.mat_khau.text()}', {int(self.tinh_trang.text())})"""
                            self.mycursor.execute(command)
                            self.mycursor.commit()
                            self.ten_giang_vien.clear()
                            self.ten_tai_khoan.clear()
                            self.mat_khau.clear()
                            self.tinh_trang.clear()
                            msg.setInformativeText("Thêm giáo viên thành công")
                        else:
                            msg.setInformativeText("Tên tài khoản này đã có trong danh sách")
                    else:
                        msg.setInformativeText("Tình trạng giảng viên không hợp lệ")
                else:
                    msg.setInformativeText("Vui lòng nhập Mật khẩu")
            else:
                msg.setInformativeText("Vui lòng nhập tên tài khoản")
        else:
            msg.setInformativeText("Vui lòng nhập tên giáo viên")
        msg.show()

    def DatMacDinh(self):
        self.ten_giang_vien.clear()
        self.ten_tai_khoan.clear()
        self.mat_khau.clear()
        self.tinh_trang.clear()