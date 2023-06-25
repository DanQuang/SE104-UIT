from admin.ui_man_hinh_them_mon_hoc import Ui_man_hinh_them_mon_hoc
from PyQt6 import QtWidgets

class Man_hinh_them_mon_hoc(QtWidgets.QWidget, Ui_man_hinh_them_mon_hoc):
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
        ten_mon_hoc = self.ten_mon_hoc.text()
        command = f"""select count(MaMonHoc)
                    from MONHOC
                    where TenMonHoc = N'{ten_mon_hoc}'"""
        
        result = int(self.mycursor.execute(command).fetchall()[0][0])
        if result == 0:
            command = f"""insert into MONHOC values(N'{ten_mon_hoc}')"""
            self.mycursor.execute(command)
            self.mycursor.commit()
            self.ten_mon_hoc.clear()
            msg.setInformativeText("Thêm môn học thành công")
        else:
            msg.setInformativeText("Tên môn học này đã có trong danh sách")
        msg.show()

    def DatMacDinh(self):
        self.ten_mon_hoc.clear()