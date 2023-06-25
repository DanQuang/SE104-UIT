from admin.ui_man_hinh_sua_do_kho import Ui_man_hinh_sua_do_kho
from PyQt6 import QtWidgets

class Man_hinh_sua_do_kho(QtWidgets.QWidget, Ui_man_hinh_sua_do_kho):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.par.conn.cursor()
        self.ma_do_kho = None
        self.setFixedSize(400, 300)
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.par.DatMacDinh()
        self.close()

    def Sua(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        ten_do_kho = self.ten_do_kho.text()
        if ten_do_kho != '':
            command = f"""select count(MaDoKho)
                    from DOKHO
                    where TenDoKho = N'{ten_do_kho}'"""
        
            result = int(self.mycursor.execute(command).fetchall()[0][0])
            if result == 0:
                command = f"""update DOKHO
                            set TenDoKho = N'{ten_do_kho}'
                            where MaDoKho = {self.ma_do_kho}"""
                self.mycursor.execute(command)
                self.mycursor.commit()
                self.ten_do_kho.clear()
                msg.setInformativeText("Thay đổi thông tin độ khó thành công")
            else:
                msg.setInformativeText("Tên độ khó này đã có trong danh sách")
        else:
            msg.setInformativeText("Vui lòng nhập tên độ khó")
        msg.show()

    def DatMacDinh(self, ma_do_kho):
        self.ma_do_kho = ma_do_kho
        self.ten_do_kho.clear()

        command = f"""select TenDoKho
                    from DOKHO
                    where MaDoKho = {self.ma_do_kho}"""
        result = self.mycursor.execute(command).fetchall()
        self.ten_do_kho.setText(str(result[0][0]))