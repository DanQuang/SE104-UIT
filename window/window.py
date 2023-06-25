from window.man_hinh_chinh import man_hinh_chinh
from window.danh_sach_cau_hoi import danh_sach_cau_hoi
from window.danh_sach_de_thi import danh_sach_de_thi
from window.danh_sach_ket_qua_cham_thi import danh_sach_ket_qua_cham_thi
from window.bao_cao_nam import man_hinh_bao_cao_nam

from PyQt6 import QtWidgets, QtCore


class Window(QtWidgets.QStackedWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.par = parent
        self.setFixedSize(960, 540)
        self.ManHinhChinh = man_hinh_chinh.Man_hinh_chinh(self)
        self.ManHinhCauHoi = danh_sach_cau_hoi.Danh_sach_cau_hoi(self)
        self.ManHinhDeThi = danh_sach_de_thi.Danh_sach_de_thi(self)
        self.ManHinhChamThi = danh_sach_ket_qua_cham_thi.Danh_sach_ket_qua_cham_thi(self)
        self.ManHinhBaoCaoNam = man_hinh_bao_cao_nam.Man_hinh_bao_cao_nam(self)
        
        self.addWidget(self.ManHinhChinh)
        self.addWidget(self.ManHinhCauHoi)
        self.addWidget(self.ManHinhDeThi)
        self.addWidget(self.ManHinhChamThi)
        self.addWidget(self.ManHinhBaoCaoNam)

        self.setCurrentIndex(0)


    def switch_ManHinhChinh(self):
        self.setFixedSize(960, 540)
        self.setCurrentIndex(0)

    def switch_ManHinhCauHoi(self):
        self.ManHinhCauHoi.ManHinhDanhSachCauHoi.DatMacDinh()
        self.setFixedSize(960, 540)
        self.setCurrentIndex(1)
    
    def switch_ManHinhDeThi(self):
        self.ManHinhDeThi.ManHinhDanhSachDeThi.DatMacDinh()
        self.setFixedSize(960, 540)
        self.setCurrentIndex(2)
    

    def switch_ManHinhChamThi(self):
        self.ManHinhChamThi.ManHinhDanhSachKetQuaChamThi.DatMacDinh()
        self.setFixedSize(960, 540)
        self.setCurrentIndex(3)

    def switch_ManHinhBaoCaoNam(self):
        self.ManHinhBaoCaoNam.DatMacDinh()
        self.setFixedSize(960, 540)
        self.setCurrentIndex(4)

    
