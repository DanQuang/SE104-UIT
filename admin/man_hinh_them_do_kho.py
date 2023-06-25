from admin.ui_man_hinh_them_do_kho import Ui_man_hinh_them_do_kho
from PyQt6 import QtWidgets

class Man_hinh_them_do_kho(QtWidgets.QWidget, Ui_man_hinh_them_do_kho):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.par.conn.cursor()
        self.setFixedSize(400, 300)
        self.thoat.clicked.connect(self.Thoat)
        self.them.clicked.connect(self.Them)

    def Thoat(self):
        self.par.DatMacDinh()
        self.close()

    def Them(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        ten_do_kho = self.ten_do_kho.text()
        command = f"""select count(MaDoKho)
                    from DOKHO
                    where TenDoKho = N'{ten_do_kho}'"""
        
        result = int(self.mycursor.execute(command).fetchall()[0][0])
        if result == 0:
            command = f"""insert into DOKHO values(N'{ten_do_kho}')"""
            self.mycursor.execute(command)
            self.mycursor.commit()
            self.ten_do_kho.clear()
            msg.setInformativeText("Thêm độ khó thành công")
        else:
            msg.setInformativeText("Tên độ khó này đã có trong danh sách")
        msg.show()

    def DatMacDinh(self):
        self.ten_do_kho.clear()