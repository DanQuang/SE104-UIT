from admin.ui_man_hinh_sua_admin import Ui_man_hinh_sua_admin
from PyQt6 import QtWidgets

class Man_hinh_sua_admin(QtWidgets.QWidget, Ui_man_hinh_sua_admin):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.par.conn.cursor()
        self.setFixedSize(400, 300)
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.par.DatMacDinh()
        self.close()

    def Sua(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        ten_tai_khoan = self.ten_tai_khoan.text()
        mat_khau = self.mat_khau.text()
        if ten_tai_khoan != '':
            if mat_khau != '':
                command = f"""update ADMIN
                            set TenTaiKhoan = N'{ten_tai_khoan}', MatKhau = N'{mat_khau}'"""
                self.mycursor.execute(command)
                self.mycursor.commit()
                self.ten_tai_khoan.clear()
                self.mat_khau.clear()
                msg.setInformativeText("Thay đổi thông tin admin thành công")
            else:
                msg.setInformativeText("Vui lòng nhập mật khẩu")
        else:
            msg.setInformativeText("Vui lòng nhập tên tài khoản")
        msg.show()

    def DatMacDinh(self):
        self.ten_tai_khoan.clear()
        self.mat_khau.clear()

        command = """select TenTaiKhoan, MatKhau
                    from ADMIN"""
        result = self.mycursor.execute(command).fetchall()
        self.ten_tai_khoan.setText(str(result[0][0]))
        self.mat_khau.setText(str(result[0][1]))