from admin.ui_man_hinh_sua_nam_hoc import Ui_man_hinh_sua_nam_hoc
from PyQt6 import QtWidgets

class Man_hinh_sua_nam_hoc(QtWidgets.QWidget, Ui_man_hinh_sua_nam_hoc):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.par = parent
        self.mycursor = parent.par.par.conn.cursor()
        self.ma_nam_hoc = None
        self.setFixedSize(400, 300)
        self.thoat.clicked.connect(self.Thoat)
        self.sua.clicked.connect(self.Sua)

    def Thoat(self):
        self.par.DatMacDinh()
        self.close()

    def Sua(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Thông báo")
        ten_nam_hoc = self.ten_nam_hoc.text()
        if ten_nam_hoc != '':
            command = f"""select count(MaNamHoc)
                    from NAMHOC
                    where TenNamHoc = N'{ten_nam_hoc}'"""
        
            result = int(self.mycursor.execute(command).fetchall()[0][0])
            if result == 0:
                command = f"""update NAMHOC
                            set TenNamHoc = N'{ten_nam_hoc}'
                            where MaNamHoc = {self.ma_nam_hoc}"""
                self.mycursor.execute(command)
                self.mycursor.commit()
                self.ten_nam_hoc.clear()
                msg.setInformativeText("Thay đổi thông tin năm học thành công")
            else:
                msg.setInformativeText("Tên năm học này đã có trong danh sách")
        else:
            msg.setInformativeText("Vui lòng nhập tên năm học")
        msg.show()

    def DatMacDinh(self, ma_nam_hoc):
        self.ma_nam_hoc = ma_nam_hoc
        self.ten_nam_hoc.clear()

        command = f"""select TenNamHoc
                    from NAMHOC
                    where MaNamHoc = {self.ma_nam_hoc}"""
        result = self.mycursor.execute(command).fetchall()
        self.ten_nam_hoc.setText(str(result[0][0]))