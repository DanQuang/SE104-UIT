import PyQt6.QtWidgets
from dang_nhap.ui_man_hinh_dang_nhap import Ui_man_hinh_dang_nhap
from PyQt6.QtCore import Qt

class Man_hinh_dang_nhap(PyQt6.QtWidgets.QWidget, Ui_man_hinh_dang_nhap):
    def __init__(self, parent= None):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.par = parent

        self.dang_nhap.clicked.connect(self.DangNhap)
        self.thoat.clicked.connect(self.Thoat)
        self.hien_mat_khau.stateChanged.connect(self.HienMatKhau)

    def DangNhap(self):
        msg = PyQt6.QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo đăng nhập")
        tai_khoan = self.tai_khoan.text()
        mat_khau = self.mat_khau.text()
        cursor = self.par.conn.cursor()

        # Duyệt qua Admin
        command = """select TenTaiKhoan, MatKhau
                    from ADMIN"""
        result = cursor.execute(command).fetchall()

        for taikhoan in result:
            if (tai_khoan == taikhoan[0]) and (mat_khau == taikhoan[1]):
                self.par.show_HeThong()
                break
        else:
            command = """select Gmail, MatKhau, TinhTrang
                    from GIANGVIEN"""
            result = cursor.execute(command).fetchall()
            for taikhoan in result:
                if (tai_khoan == taikhoan[0]) and (mat_khau == taikhoan[1]):
                    if (int(taikhoan[2]) == 1):
                        # Lấy ra mã giảng viên của giảng viên đăng nhập vào
                        command = f"""select MaGiangVien
                                    from GIANGVIEN
                                    where Gmail = N'{tai_khoan}'
                                    and MatKhau = N'{mat_khau}'"""
                        self.par.MaGiangVien = int(cursor.execute(command).fetchall()[0][0])
                        self.par.show_Window()
                        break
                    else:
                        msg.setText("Tài khoản của bạn đã bị vô hiệu hóa")
                        msg.resize(600, 300)
                        msg.exec()
                        break
            else:
                msg.setText("Thông tin đăng nhập không chính xác!")
                msg.resize(600, 300)
                msg.exec()
        
    def Thoat(self):
        self.close()

    def HienMatKhau(self, checked):
        if checked:
            self.mat_khau.setEchoMode(PyQt6.QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.mat_khau.setEchoMode(PyQt6.QtWidgets.QLineEdit.EchoMode.Password)

    def DatMacDinh(self):
        self.tai_khoan.setText("")
        self.mat_khau.setText("")
        self.mat_khau.setEchoMode(PyQt6.QtWidgets.QLineEdit.EchoMode.Password)