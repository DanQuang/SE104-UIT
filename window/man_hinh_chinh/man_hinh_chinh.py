from PyQt6 import QtWidgets
from window.man_hinh_chinh.ui_man_hinh_chinh import Ui_man_hinh_chinh

class Man_hinh_chinh(QtWidgets.QWidget, Ui_man_hinh_chinh):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.setFixedSize(960, 540)
        
        self.dang_xuat.clicked.connect(self.DangXuat)
        self.danh_sach_cau_hoi.clicked.connect(self.DanhSachCauHoi)
        self.danh_sach_de_thi.clicked.connect(self.DanhSachDeThi)
        self.danh_sach_cham_thi.clicked.connect(self.DanhSachChamThi)
        self.bao_cao_nam.clicked.connect(self.BaoCaoNam)

    def DangXuat(self):
        par = self.window()
        par.par.show_ManHinhDangNhap()

    def DanhSachCauHoi(self):
        par = self.window()
        par.switch_ManHinhCauHoi()

    def DanhSachDeThi(self):
        par = self.window()
        par.switch_ManHinhDeThi()

    def DanhSachChamThi(self):
        par = self.window()
        par.switch_ManHinhChamThi()

    def BaoCaoNam(self):
        par = self.window()
        par.switch_ManHinhBaoCaoNam()

    

    
