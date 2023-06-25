from admin.ui_man_hinh_sua_giang_vien import Ui_man_hinh_sua_giang_vien
from PyQt6 import QtWidgets

class Man_hinh_sua_giang_vien(QtWidgets.QWidget, Ui_man_hinh_sua_giang_vien):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.par.conn.cursor()
        self.ma_giang_vien = None
        self.setFixedSize(400, 300)
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.par.DatMacDinh()
        self.close()

    def Sua(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        mat_khau = self.mat_khau.text()
        tinh_trang = self.tinh_trang.text()
        if mat_khau != '':
            if self.tinh_trang.text() != '' and self.tinh_trang.text().isnumeric():
                command = f"""update GIANGVIEN
                            set MatKhau = N'{mat_khau}', TinhTrang = {int(self.tinh_trang.text())}
                            where MaGiangVien = {self.ma_giang_vien}"""
                self.mycursor.execute(command)
                self.mycursor.commit()
                self.ten_giang_vien.clear()
                self.ten_tai_khoan.clear()
                self.mat_khau.clear()
                self.tinh_trang.clear()
                msg.setInformativeText("Chỉnh sửa giảng viên thành công")
            else:
                msg.setInformativeText("ình trạng giảng viên không hợp lệ")
        else:
            msg.setInformativeText("Vui lòng nhập mật khẩu")
        msg.show()

    def DatMacDinh(self, ma_giang_vien):
        self.ma_giang_vien = ma_giang_vien
        self.ten_giang_vien.clear()
        self.ten_tai_khoan.clear()
        self.mat_khau.clear()

        command = f"""select TenGiangVien, Gmail, MatKhau, TinhTrang
                    from GIANGVIEN
                    where MaGiangVien = {self.ma_giang_vien}"""
        result = self.mycursor.execute(command).fetchall()
        self.ten_giang_vien.setText(str(result[0][0]))
        self.ten_tai_khoan.setText(str(result[0][1]))
        self.mat_khau.setText(str(result[0][2]))
        self.tinh_trang.setText(str(result[0][3]))

        self.ten_giang_vien.setEnabled(False)
        self.ten_tai_khoan.setEnabled(False)