from window.danh_sach_cau_hoi.man_hinh_danh_sach_cau_hoi import Man_hinh_danh_sach_cau_hoi
from window.danh_sach_cau_hoi.man_hinh_soan_cau_hoi import Man_hinh_soan_cau_hoi
from window.danh_sach_cau_hoi.man_hinh_sua_cau_hoi import Man_hinh_sua_cau_hoi
from PyQt6 import QtWidgets

class Danh_sach_cau_hoi(QtWidgets.QStackedWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.par = parent
        self.setFixedSize(960, 540)

        self.ManHinhDanhSachCauHoi = Man_hinh_danh_sach_cau_hoi(self)
        self.ManHinhSoanCauHoi = Man_hinh_soan_cau_hoi(self)
        self.ManHinhSuaCauHoi = Man_hinh_sua_cau_hoi(self)

        self.addWidget(self.ManHinhDanhSachCauHoi)
        self.addWidget(self.ManHinhSoanCauHoi)
        self.addWidget(self.ManHinhSuaCauHoi)

        self.setCurrentIndex(0)

    def switch_ManHinhDanhSachCauHoi(self):
        self.ManHinhDanhSachCauHoi.DatMacDinh()
        self.setCurrentIndex(0)

    def switch_ManHinhSoanCauHoi(self):
        self.ManHinhSoanCauHoi.DatMacDinh()
        self.setCurrentIndex(1)

    def switch_ManHinhSuaCauHoi(self, ma_cau_hoi):
        self.ManHinhSuaCauHoi.DatMacDinh(ma_cau_hoi)
        self.setCurrentIndex(2)
