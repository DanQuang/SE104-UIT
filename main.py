from PyQt6.QtWidgets import QApplication
from window import window
from admin.man_hinh_quan_ly_he_thong import Man_hinh_quan_ly_he_thong
from dang_nhap import man_hinh_dang_nhap

import pyodbc
import sys

class App():
    def __init__(self):
        super().__init__()
        self.conn = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=DESKTOP-MDSLP1R;'
                'Database=QLRDCT;'
            )
        self.MaGiangVien = 0

        self.Window = window.Window(self)
        self.HeThong = Man_hinh_quan_ly_he_thong(self)
        self.ManHinhDangNhap = man_hinh_dang_nhap.Man_hinh_dang_nhap(self)
        

        self.show_ManHinhDangNhap()

    def show_ManHinhDangNhap(self):
        try:
            self.Window.close()
            self.HeThong.close()
            self.ManHinhDangNhap.DatMacDinh()
            self.ManHinhDangNhap.show()
        except:
            self.ManHinhDangNhap.show()

    def show_Window(self):
        self.ManHinhDangNhap.close()
        self.Window.show()

    def show_HeThong(self):
        self.ManHinhDangNhap.close()
        self.HeThong.DatMacDinh()
        self.HeThong.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = App()

    sys.exit(app.exec())
