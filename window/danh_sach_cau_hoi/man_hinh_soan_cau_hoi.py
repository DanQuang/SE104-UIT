from PyQt6 import QtWidgets
from window.danh_sach_cau_hoi.ui_man_hinh_soan_cau_hoi import Ui_man_hinh_soan_cau_hoi

class Man_hinh_soan_cau_hoi(QtWidgets.QWidget, Ui_man_hinh_soan_cau_hoi):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mycursor = self.par.par.par.conn.cursor()
        self.DatMacDinh()

        self.setFixedSize(960, 540)
        
        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)


    def Thoat(self):
        self.par.switch_ManHinhDanhSachCauHoi()

    def Them(self):
        # Tạo message
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")

        # Lấy các giá trị cần thêm vào
        mon_hoc = self.mon_hoc.currentText()
        do_kho = self.do_kho.currentText()
        cau_hoi = self.cau_hoi.toPlainText()
        cau_tra_loi = self.cau_tra_loi.toPlainText()
        try:
            if (cau_hoi != ''):
                if (cau_tra_loi != ''):
                    #Lấy mã môn học và mã độ khó ra
                    command = f"""select MaMonHoc
                                from MONHOC
                                where MONHOC.TenMonHoc = N'{mon_hoc}' """
                    ma_mon_hoc = int(self.mycursor.execute(command).fetchall()[0][0])

                    command = f"""select MaDoKho
                                from DOKHO
                                where DOKHO.TenDoKho = N'{do_kho}' """
                    ma_do_kho = int(self.mycursor.execute(command).fetchall()[0][0])

                    # Thêm câu hỏi vào dữ liệu
                    command = f"""INSERT INTO CAUHOI
                                VALUES ({ma_mon_hoc}, {ma_do_kho}, N'{cau_hoi}', N'{cau_tra_loi}' )"""
                    
                    self.mycursor.execute(command)
                    self.mycursor.commit()
                    msg.setInformativeText("Thêm câu hỏi thành công")
                    self.cau_hoi.clear()
                    self.cau_tra_loi.clear()
                else:
                    msg.setInformativeText("Vui lòng nhập câu trả lời")
            else:
                msg.setInformativeText("Vui lòng nhập câu hỏi")
        except:
            msg.setInformativeText("Thêm câu hỏi thất bại")
        msg.show()

    def DatMacDinh(self):
        self.mon_hoc.clear()
        self.do_kho.clear()

        self.MaGiangVien = self.par.par.par.MaGiangVien
        # Thêm giá trị vào combobox môn học
        command = f"""select TenMonHoc
                    from GIANGVIEN g, CT_GIANGVIEN ct, MONHOC m
                    where g.MaGiangVien = ct.MaGiangVien
                    and ct.MaMonHoc = m.MaMonHoc
                    and g.MaGiangVien = {self.MaGiangVien}"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.mon_hoc.addItem(row[0])

        # Thêm giá trị vào combobox độ khó
        command = """select TenDoKho
                    from DOKHO"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.do_kho.addItem(row[0])
        
        self.mon_hoc.setCurrentIndex(-1)
        self.do_kho.setCurrentIndex(-1)

        self.cau_hoi.clear()
        self.cau_tra_loi.clear()