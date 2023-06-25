from window.danh_sach_de_thi.man_hinh_danh_sach_de_thi import Man_hinh_danh_sach_de_thi
from window.danh_sach_de_thi.man_hinh_soan_de_thi import Man_hinh_soan_de_thi
from window.danh_sach_de_thi.man_hinh_sua_de_thi import Man_hinh_sua_de_thi
from PyQt6 import QtWidgets

class Danh_sach_de_thi(QtWidgets.QStackedWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.par = parent
        self.setFixedSize(960, 540)

        self.ManHinhDanhSachDeThi = Man_hinh_danh_sach_de_thi(self)
        self.ManHinhSoanDeThi = Man_hinh_soan_de_thi(self)
        self.ManHinhSuaDeThi = Man_hinh_sua_de_thi(self)

        self.addWidget(self.ManHinhDanhSachDeThi)
        self.addWidget(self.ManHinhSoanDeThi)
        self.addWidget(self.ManHinhSuaDeThi)

        self.setCurrentIndex(0)

    def switch_ManHinhDanhSachDeThi(self):
        self.ManHinhDanhSachDeThi.DatMacDinh()
        self.setCurrentIndex(0)

    def switch_ManHinhSoanDeThi(self):
        self.ManHinhSoanDeThi.DatMacDinh()
        self.setCurrentIndex(1)

    def switch_ManHinhSuaDeThi(self, ma_de_thi):
        self.ManHinhSuaDeThi.DatMacDinh(ma_de_thi)
        self.setCurrentIndex(2)