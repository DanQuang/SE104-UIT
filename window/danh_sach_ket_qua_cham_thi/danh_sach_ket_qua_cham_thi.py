from window.danh_sach_ket_qua_cham_thi.man_hinh_danh_sach_ket_qua_cham_thi import Man_hinh_danh_sach_ket_qua_cham_thi
from window.danh_sach_ket_qua_cham_thi.man_hinh_lap_ket_qua_cham_thi import Man_hinh_lap_ket_qua_cham_thi
from window.danh_sach_ket_qua_cham_thi.man_hinh_sua_ket_qua_cham_thi import Man_hinh_sua_ket_qua_cham_thi
from PyQt6 import QtWidgets

class Danh_sach_ket_qua_cham_thi(QtWidgets.QStackedWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.par = parent
        self.setFixedSize(960, 540)

        self.ManHinhDanhSachKetQuaChamThi = Man_hinh_danh_sach_ket_qua_cham_thi(self)
        self.ManHinhSoanKetQuaChamThi = Man_hinh_lap_ket_qua_cham_thi(self)
        self.ManHinhSuaKetQuaChamThi = Man_hinh_sua_ket_qua_cham_thi(self)

        self.addWidget(self.ManHinhDanhSachKetQuaChamThi)
        self.addWidget(self.ManHinhSoanKetQuaChamThi)
        self.addWidget(self.ManHinhSuaKetQuaChamThi)    

        self.setCurrentIndex(0)

    def switch_ManHinhDanhSachKetQuaChamThi(self):
        self.ManHinhDanhSachKetQuaChamThi.DatMacDinh()
        self.setFixedSize(960, 540)
        self.setCurrentIndex(0)

    def switch_ManHinhLapKetQuaChamThi(self):
        self.ManHinhSoanKetQuaChamThi.DatMacDinh()
        self.setFixedSize(960, 540)
        self.setCurrentIndex(1)

    def switch_ManHinhSuaKetQuaChamThi(self, ket_qua_cham_thi):
        self.ManHinhSuaKetQuaChamThi.DatMacDinh(ket_qua_cham_thi)
        self.setFixedSize(960, 540)
        self.setCurrentIndex(2)
