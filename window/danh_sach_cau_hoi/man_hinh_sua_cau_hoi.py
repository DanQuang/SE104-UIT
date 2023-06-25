from PyQt6 import QtWidgets
from window.danh_sach_cau_hoi.ui_man_hinh_sua_cau_hoi import Ui_man_hinh_sua_cau_hoi

class Man_hinh_sua_cau_hoi(QtWidgets.QWidget, Ui_man_hinh_sua_cau_hoi):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.par = parent
        self.mycursor = self.par.par.par.conn.cursor()

        # Các yếu tố không được sửa trong câu
        self.ma_cau_hoi = None
        self.ma_mon_hoc = None

        # Thêm giá trị vào combobox môn học
        command = """select TenMonHoc
                    from MONHOC"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.mon_hoc.addItem(row[0])

        # Thêm giá trị vào combobox độ khó
        command = """select TenDoKho
                    from DOKHO"""
        result = self.mycursor.execute(command).fetchall()

        for row in result:
            self.do_kho.addItem(row[0])
        
        # Chức năng các nút
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)


    def Thoat(self):
        self.par.switch_ManHinhDanhSachCauHoi()

    def Sua(self):
        # Lấy các giá trị cần sửa vào
        do_kho = self.do_kho.currentText()
        cau_hoi = self.cau_hoi.toPlainText()
        cau_tra_loi = self.cau_tra_loi.toPlainText()

        # Tạo message
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")

        if (cau_hoi != ''):
            if (cau_tra_loi != ''):
                # Tạo message
                msg_1 = QtWidgets.QMessageBox(self)
                msg_1.setWindowTitle("Thông báo")
                msg_1.setInformativeText("Bạn có chắc chắn muốn sửa câu hỏi này không?")
                msg_1.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
                msg_1.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)
                button_clicked = msg_1.exec()

                # Nếu người dùng chọn Ok thì bắt đầu sửa
                if button_clicked == QtWidgets.QMessageBox.StandardButton.Ok:
                    # Lấy mã độ khó
                    command = f"""select MaDoKho
                                from DOKHO
                                where DOKHO.TenDoKho = N'{do_kho}' """
                    ma_do_kho = int(self.mycursor.execute(command).fetchall()[0][0])

                    # Cập nhập thông tin cho câu hỏi
                    command = f"""update CAUHOI
                            set MaMonHoc = {self.ma_mon_hoc}, MaDoKho = {ma_do_kho}, NoiDungCauHoi = N'{cau_hoi}', NoiDungCauTraLoi = N'{cau_tra_loi}'
                            where MaCauHoi = {self.ma_cau_hoi} """
                    self.mycursor.execute(command)
                    self.mycursor.commit()
                    msg.setInformativeText("Sửa câu hỏi thành công")
            else:
                msg.setInformativeText("Vui lòng nhập câu trả lời")
        else:
            msg.setInformativeText("Vui lòng nhập câu hỏi")
        msg.show()


    def DatMacDinh(self, ma_cau_hoi):
        self.ma_cau_hoi = ma_cau_hoi
        self.setFixedSize(960, 540)

        # Lấy các thông tin của câu hỏi ra
        command = f"""select MaMonHoc, MaDoKho, NoiDungCauHoi, NoiDungCauTraLoi
                    from CAUHOI 
                    where MaCauHoi = {ma_cau_hoi}"""
        result = self.mycursor.execute(command).fetchall()

        # Lấy ra các yếu tố để hiển thị
        self.ma_mon_hoc = int(result[0][0])
        ma_do_kho = int(result[0][1])
        noi_dung_cau_hoi = result[0][2]
        noi_dung_cau_tra_loi = result[0][3]

        # Lấy ra tên môn học
        command = f"""select TenMonHoc
                    from MONHOC
                    where MaMonHoc = {self.ma_mon_hoc}"""
        ten_mon_hoc = self.mycursor.execute(command).fetchall()[0][0]

        # Lây ra tên độ khó
        command = f"""select TenDoKho
                    from DOKHO
                    where MaDoKho = {ma_do_kho}"""
        ten_do_kho = self.mycursor.execute(command).fetchall()[0][0]

        self.mon_hoc.setCurrentText(f"{ten_mon_hoc}")
        # Không cho người dùng thay đổi môn học
        self.mon_hoc.setEnabled(False)

        self.do_kho.setCurrentText(f"{ten_do_kho}")
        
        self.cau_hoi.setText(noi_dung_cau_hoi)
        self.cau_tra_loi.setText(noi_dung_cau_tra_loi)