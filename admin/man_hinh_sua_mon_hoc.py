from admin.ui_man_hinh_sua_mon_hoc import Ui_man_hinh_sua_mon_hoc
from PyQt6 import QtWidgets

class Man_hinh_sua_mon_hoc(QtWidgets.QWidget, Ui_man_hinh_sua_mon_hoc):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.par.conn.cursor()
        self.ma_mon_hoc = None
        self.setFixedSize(400, 300)
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.par.DatMacDinh()
        self.close()

    def Sua(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        ten_mon_hoc = self.ten_mon_hoc.text()
        if ten_mon_hoc != '':
            command = f"""select count(MaMonHoc)
                    from MONHOC
                    where TenMonHoc = N'{ten_mon_hoc}'"""
        
            result = int(self.mycursor.execute(command).fetchall()[0][0])
            if result == 0:
                command = f"""update MONHOC
                            set TenMonHoc = N'{ten_mon_hoc}'
                            where MaMonHoc = {self.ma_mon_hoc}"""
                self.mycursor.execute(command)
                self.mycursor.commit()
                self.ten_mon_hoc.clear()
                msg.setInformativeText("Thay đổi thông tin môn học thành công")
            else:
                msg.setInformativeText("Tên môn học này đã có trong danh sách")
        else:
            msg.setInformativeText("Vui lòng nhập tên môn học")
        msg.show()

    def DatMacDinh(self, ma_mon_hoc):
        self.ma_mon_hoc = ma_mon_hoc
        self.ten_mon_hoc.clear()

        command = f"""select TenMonHoc
                    from MONHOC
                    where MaMonHoc = {self.ma_mon_hoc}"""
        result = self.mycursor.execute(command).fetchall()
        self.ten_mon_hoc.setText(str(result[0][0]))