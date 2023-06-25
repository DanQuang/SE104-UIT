CREATE DATABASE QLRDCT;

--create database test2
create table CT_KETQUACHAMTHI
(
	MaKQChamThi int,
	MSSV int,
	DiemSo float not null,
	DiemChu Nvarchar(200) not null,
	GhiChu Nvarchar(200) not null,
	constraint PK_CT_KETQUACHAMTHI primary key (MaKQChamThi, MSSV)
)

create table SINHVIEN 
(
	MSSV int IDENTITY(1,1),
	TenSinhVien Nvarchar(200) not null,
	constraint PK_SINHVIEN primary key (MSSV)
)

create table THAMSO
(
	TenThamSo Nvarchar(200),
	GiaTri float not null,
	constraint PK_THAMSO primary key (TenThamSo)
)

create table KETQUACHAMTHI
(
	MaKQChamThi int IDENTITY(1,1),
	MaDeThi int not null,
	MaLop int not null,
	MaGiangVien int not null,
	TongSoBaiCham int not null,
	constraint PK_KETQUACHAMTHI primary key (MaKQChamThi)
)

create table GIANGVIEN 
(
	MaGiangVien int IDENTITY(1,1),
	TenGiangVien Nvarchar(200) not null,
	Gmail Nvarchar(200) not null,
	MatKhau Nvarchar(200) not null,
	TinhTrang int not null
	constraint PK_GIANGVIEN primary key (MaGiangVien)
)

create table LOPHOC 
(
	MaLop int IDENTITY(1,1),
	TenLop Nvarchar(200) not null, 
	constraint PK_LOPHOC primary key (MaLop)
)

create table DETHI
(
	MaDeTHi int IDENTITY(1,1),
	MaGiangVien int not null,
	MaHocKy int not null,
	MaNamHoc int not null,
	MaMonHoc int not null,
	ThoiLuong int not null, 
	TieuDe nvarchar(100) not null,
	NgayThi Date not null,
	SoCau int not null, 
	constraint PK_DETHI primary key (MaDeThi)
)
SELECT CONVERT(varchar, NgayThi, 103) AS FormattedDate
FROM DETHI

create table NAMHOC
(
	MaNamHoc int IDENTITY(1,1),
	TenNamHoc Nvarchar(200) not null,
	constraint PK_NAMHOC primary key (MaNamHoc)
)

create table HOCKY
(
	MaHocKy int IDENTITY(1,1),
	TenHocKy Nvarchar(200) not null,
	constraint PK_HOCKY primary key (MaHocKy)
)

create table CT_DETHI
(
	MaDeThi int,
	MaCauHoi int,
	Diem float,
	constraint PK_CT_DETHI primary key (MaDeThi, MaCauHoi)
)

create table CAUHOI
(
	MaCauHoi int IDENTITY(1,1),
	MaMonHoc int not null,
	MaDoKho int not null,
	NoiDungCauHoi nvarchar(1000) not null,
	NoiDungCauTraLoi nvarchar(2000) not null,
	constraint PK_CAUHOI primary key (MaCauHoi)
)

create table MONHOC
(
	MaMonHoc int IDENTITY(1,1),
	TenMonHoc Nvarchar(200) not null,
	constraint PK_MONHOC primary key (MaMonHoc)
)

create table DOKHO
(
	MaDoKho int IDENTITY(1,1),
	TenDoKho Nvarchar(200) not null,
	constraint PK_DOKHO primary key (MaDoKho)
)

create table CT_LOPHOC
(
	MaLop int,
	MSSV int
	constraint PK_CT_LOPHOC primary key (MaLop, MSSV)
)
create table CT_GIANGVIEN
(
	MaGiangVien int,
	MaMonHoc int,
	constraint PK_CT_GIANGVIEN primary key (MaGiangVien, MaMonHoc)
)
alter table CT_GIANGVIEN add constraint FK_CT_GIANGVIEN_GIANGVIEN foreign key (MaGiangVien) references GIANGVIEN (MaGiangVien)
alter table CT_GIANGVIEN add constraint FK_CT_GIANGVIEN_MONHOC foreign key (MaMonHoc) references MONHOC (MaMonHoc)

alter table CT_KETQUACHAMTHI add constraint FK_KETQUACHAMTHI_SINHVIEN foreign key (MSSV) references SINHVIEN (MSSV)
alter table CT_KETQUACHAMTHI add constraint FK_KETQUACHAMTHI_KETQUACHAMTHI foreign key (MaKQChamThi) references KETQUACHAMTHI (MaKQChamThi)

alter table KETQUACHAMTHI add constraint FK_KETQUACHAMTHI_GIANGVIEN foreign key (MaGiangVien) references GIANGVIEN (MaGiangVien)
alter table KETQUACHAMTHI add constraint FK_KETQUACHAMTHI_LOPHOC foreign key (MaLop) references LOPHOC (MaLop)
alter table KETQUACHAMTHI add constraint FK_KETQUACHAMTHI_DETHI foreign key (MaDeThi) references DETHI (MaDeThi)

alter table DETHI add constraint FK_DETHI_NAMHOC foreign key (MaNamHoc) references NAMHOC (MaNamHoc)
alter table DETHI add constraint FK_DETHI_HOCKY foreign key (MaHocKy) references HOCKY (MaHocKy)
alter table DETHI add constraint FK_DETHI_MONHOC foreign key (MaMonHoc) references MONHOC (MaMonHoc)
alter table DETHI add constraint FK_DETHI_GIANGVIEN foreign key (MaGiangVien) references GIANGVIEN (MaGiangVien)

alter table CT_DETHI add constraint FK_CT_DETHI_CAUHOI foreign key (MaCauHoi) references CAUHOI (MaCauHoi)
alter table CT_DETHI add constraint FK_CT_DETHI_DETHI foreign key (MaDeThi) references DETHI (MaDeThi)

alter table CAUHOI add constraint FK_CAUHOI_MONHOC foreign key (MaMonHoc) references MONHOC (MaMonHoc)
alter table CAUHOI add constraint FK_CAUHOI_DOKHO foreign key (MaDoKho) references DOKHO (MaDoKho)

alter table CT_LOPHOC add constraint FK_LOPHOC_SINHVIEN foreign key (MSSV) references SINHVIEN (MSSV)
alter table CT_LOPHOC add constraint FK_LOPHOC_LOPHOC foreign key (MaLop) references LOPHOC (MaLop)

create table ADMIN
(
	MaAdmin int IDENTITY(1,1),
	TenTaiKhoan nvarchar(200),
	MatKhau nvarchar(200),
	constraint PK_ADMIN primary key (MaAdmin)
)

insert into GIANGVIEN values (N'Lê Tuấn Hưng','hung@uit','hung1',1);
insert into GIANGVIEN values (N'Trương Thanh Hải','hai@uit','hai1',1);
insert into GIANGVIEN values (N'Trần Mộng Như','nhu@uit','nhu1',1);
insert into GIANGVIEN values (N'Đỗ Bảo','bao@uit','bao1',0);

insert into MONHOC values (N'Lý');
insert into MONHOC values (N'Toán');
insert into MONHOC values (N'Hóa');
insert into MONHOC values (N'Anh');

insert into CT_GIANGVIEN values (1,1);
insert into CT_GIANGVIEN values (2,2);
insert into CT_GIANGVIEN values (3,3);
insert into CT_GIANGVIEN values (1,4);

insert into DOKHO values (N'Dễ');
insert into DOKHO values (N'Trung Bình');
insert into DOKHO values (N'Phức Tạp');
insert into DOKHO values (N'Khó');

insert into NAMHOC values (N'2021-2022');
insert into NAMHOC values (N'2022-2023');

insert into HOCKY values (N'Học kỳ 1');
insert into HOCKY values (N'Học kỳ 2');

insert into CAUHOI values (1,1,N'Một chất điểm dao động điều hoà với chu kì 1,25 s và biên độ 5 cm. Tốc độ lớn nhất của chất điểm là:',N'25,1 cm/s');
insert into CAUHOI values (1,1,N'Một vật nhỏ dao động điều hòa theo phương trình x = Acos10t (t tính bằng s). Tại t = 2 s, pha của dao động là:',N'20 rad');
insert into CAUHOI values (1,1,N'Chọn một chất điểm dao động điều hòa trên đoạn thẳng MN dài 6 cm với tần số 2 Hz. Chọn gốc thời gian là lúc chất điểm có li độ 3√3/2 cm và chuyển động ngược chiều với chiều dương mà mình đã chọn. Phương trình dao động của chất điểm là:',N'x = 3cos(4πt + π/6) cm');
insert into CAUHOI values (1,1,N'Phương trình dao động của một vật dao động điều hòa là: x = - 5cos(10πt + π/6) cm. Chọn đáp án đúng:',N'Chu kì T = 0,2 s');
insert into CAUHOI values (1,1,N'Con lắc lò xo gồm vật nặng 100 gam và lò xo nhẹ độ cứng 40 N/m. Tác dụng một ngoại lực điều hòa cưỡng bức biên độ F và tần số f1 = 4 Hz theo phương trùng với trục của lò xo thì biên độ dao động ổn định A1. Nếu giữ nguyên biên độ F và tăng tần số ngoại lực đến giá trị f2 = 5 Hz thì biên độ dao động ổn định A2. So sánh A1 và A2',N'A1 > A2');
insert into CAUHOI values (1,2,N'Phát biểu nào sau đây là đúng khi nói về dao động tắt dần?',N'Dao động tắt dần có biên độ giảm dần theo thời gian');
insert into CAUHOI values (1,2,N'Dao động tắt dần là một dao động có',N'biên độ giảm dần theo thời gian');
insert into CAUHOI values (1,2,N'Biên độ dao động cưỡng bức không phụ thuộc vào',N'pha ban đầu của ngoại lực tuần hoàn tác dụng lên vật');
insert into CAUHOI values (1,2,N'Chiết suất của môi trường trong suốt đối với các ánh sáng đơn sắc trong một chùm ánh sáng trắng',N'lớn khi tần số ánh sáng lớn');
insert into CAUHOI values (1,2,N'Trong thí nghiệm Y – âng về giao thoa ánh sáng, hiệu đường đi của các sóng từ hai khe S1, S2 đến vân tối thứ ba kể từ vân trung tâm có trị số là',N'2,5λ');
insert into CAUHOI values (1,3,N'Tiến hành thí nghiệm giao thoa ánh sáng Y – âng trong không khí, khoảng vân đo được là i. Nếu đặt toàn bộ thí nghiệm trong nước có chiết suất n thì khoảng vân là',N'i/n');
insert into CAUHOI values (1,3,N'Trong thí nghiệm Y –âng về giao thoa ánh sáng, chiếu đồng thời hai bức xạ đơn sắc có λ1 = 0,6 µ và λ2 = 0,4 µm vào khe Y – âng. Khoảng giữa hai khe a = 1 mm. Khoảng cách từ hai khe đến màn D = 2 m. Khoảng cách ngắn nhất giữa các vị trí trên màn có hai vân sáng trùng nhau là',N'2,4 mm');
insert into CAUHOI values (1,3,N'Trong thí nghiệm giao thoa ánh sáng Y –âng với ánh sáng trắng (có bước sóng từ 0,4 µm đến 0,76 µm), khoảng cách từ hai khe đến màn là 2 m, bề rộng quang phổ bậc 2 thu được trên màn là 1,5 mm. Khoảng cách giữa hai khe là',N'0,96 mm');
insert into CAUHOI values (1,3,N'Trong một thí nghiệm giao thoa ánh sáng với hai khe Y – âng trong vùng MN trên màn quan sát, người ta đếm được 13 vân sáng với M và N là hai vân sáng ứng với bước sóng λ1 = 0,42 µm. Giữ nguyên điều kiện thí nghiệm, thay nguồn sáng đơn sắc với bước sóng λ2 = 0,63 µm thì số vân sáng trên đoạn có chiều dài bằng MN trên màn là',N'9');
insert into CAUHOI values (1,3,N'Một sóng cơ truyền dọc theo trục Ox có phương trình u = Acos(20πt – πx) (cm), với t tính bằng s. Tần số của sóng này bằng',N'10 Hz');
insert into CAUHOI values (1,4,N'Sóng cơ học truyền trong môi trường vật chất đồng nhất qua điểm A rồi đến điểm B thì',N'biên độ dao động tại A lớn hơn tại B');
insert into CAUHOI values (1,4,N'Đặt điện áp xoay chiều u = 311cos100πt (V) vào 2 đầu của một cuộn cảm thuần có độ tự cảm L = 1/π(H). Cường độ dòng điện hiệu dụng qua cuộn cảm có giá trị bằng',N'2,2 A');
insert into CAUHOI values (1,4,N'Mắc một cuộn cảm vào một điện áp xoay chiều có tần số f, cuộn cảm có cảm kháng là ZL. Nếu giảm độ tự cảm của cuộn cảm đi một nửa và tần số tăng lên 4 lần thì cảm kháng ZL sẽ',N'tăng 2 lần');
insert into CAUHOI values (1,4,N'Tại thời điểm t = 0,5 s cường độ dòng điên xoay chiều chạy qua mạch bằng 4A, đó là',N'Cường độ tức thời');
insert into CAUHOI values (1,4,N'Một sóng âm truyền trong không khí. Mức cường độ âm tại điểm M và tại điểm N lần lượt là 40 dB và 80 dB. Cường độ âm tại N lớn hơn cường độ âm tại M',N'10000 lần');

insert into CAUHOI values (2,1,N'Giá trị lớn nhất của hàm số y = x(5 - 2x)^2 trên [0; 3] là:',N'250/27');
insert into CAUHOI values (2,1,N'Một hành lang giữa hai tòa tháp có hình dạng một hình lăng trụ đứng. Hai mặt bên ABB’A’ và ACC’A’ là hai tấm kính hình chữ nhật dài 20m, rộng 5m. Với độ dài xấp xỉ nào của BC thì thể tích hành lang này lớn nhất',N'7m');
insert into CAUHOI values (2,1,N'Một công ti quản lí chuẩn bị xây dựng một khu chung cư mới. Họ tính toán nếu tòa nhà có x căn hộ thì chi phí bảo trì của tòa nhà là: C(x) = 4000 - 14x + 0,04x^2. Khu đất của họ có thể xây được tòa nhà chứa tối đa 300 căn hộ. Hỏi họ nên xây dựng tòa nhà có bao nhiêu căn hộ để chi phí bảo trì của tòa nhà là nhỏ nhất?',N'175');
insert into CAUHOI values (2,1,N'Tìm GTNN của hàm số y = x^2 - 3x + 5',N'11/4');
insert into CAUHOI values (2,1,N'Cho hàm số y = - x^3 + 3x^2 - 3x + 1, mệnh đề nào sau đây là đúng?',N'Hàm số luôn nghịch biến');
insert into CAUHOI values (2,2,N'Gọi M và m tương ứng là giá trị lớn nhất và giá trị nhỏ nhất của hàm số y = 2(sinx)^2 - cosx + 1 thì M.m bằng',N'0');
insert into CAUHOI values (2,2,N'Cho 2 hàm số f(x) = x^2 và g(x) = x^(1/2) . Biết rằng α > 0, f(α) < g(α). Khẳng định nào sau đây là đúng?',N'0 < α < 1');
insert into CAUHOI values (2,2,N'Cho hàm số y = x^3 - x^2 + (m-1)x + m. Tìm điều kiện của tham số m để hàm số đồng biến trên R',N'm > 2 ');
insert into CAUHOI values (2,2,N'Cho hàm số y = x^3 + 3x^2 + mx + 1 - 2m. Tìm các giá trị của m để hàm số đồng biến trên đoạn có độ dài bằng 1.',N'Không tồn tại');
insert into CAUHOI values (2,2,N'Khoảng nghịch biến của hàm số y = x^4 - 2x^2 - 1 là',N'(-∞; -1) và (0; 1)');
insert into CAUHOI values (2,3,N'Nếu log(log(log(logx))) = 0 thì x = 10k . Tìm giá trị của k',N'10^10');
insert into CAUHOI values (2,3,N'Giải phương trình log5(x + 4) = 3',N'121');
insert into CAUHOI values (2,3,N'Giải phương trình lnx + ln(x - 1) = ln2',N'x = -1, x = 2');
insert into CAUHOI values (2,3,N'Tìm m để bất phương trình x^4 + 2x^2 ≥ m luôn đúng',N'm ≤ 0');
insert into CAUHOI values (2,3,N'Tìm m để phương trình x^3 + 3x^2 = m có ba nghiệm phân biệt',N'0 < m < 4');
insert into CAUHOI values (2,4,N'Tâm đối xứng của đồ thị hàm số y = -x^3 - 3x^2 + 1 là',N'(-1; -1)');
insert into CAUHOI values (2,4,N'Cho số phức z thỏa mãn (3 + 2i)z + (2 - i)^2 = 4 + i. Môđun của số phức w = (z + 1)z− là',N'√10');
insert into CAUHOI values (2,4,N'Số phức z thỏa mãn z(1 + 2i) + 1 - i = 2i là',N'1+i');
insert into CAUHOI values (2,4,N'Tính tích tất cả các nghiệm của phương trình 3^(2x^2 + 2x + 1) - 28.3(x^2 + x) + 9 = 0',N'-2');
insert into CAUHOI values (2,4,N'Giải phương trình 3^(2x - 3) = 7 . Viết nghiệm dưới dạng thập phân, làm tròn đến hàng phần nghìn.',N'2,386');

Insert into CAUHOI values (3,1,N'Ngâm một lá Zn vào dung dịch HC1 thấy bọt khí thoát ra ít và chậm. Nếu nhỏ thêm vài giọt dung dịch X thì thấy bọt khí thoát ra rất nhiều và nhanh. Chất tan trong dung dịch X là chất nào sau đây ?',N'CuSO4');
Insert into CAUHOI values (3,1,N'Một đồng xu bảng đồng rơi trên một miếng thép. Sau một thới gian có thể quan sát dược hiện tượng nào sau dây',N'Trên miếng thép xuất hiện lớp gỉ màu nâu đỏ');
Insert into CAUHOI values (3,1,N'Nếu vật làm bằng hợp kim Fe-Zn bị ăn mòn điện hoá thì trong quá trình ăn mòn',N'Kẽm đóng vai trò anot và bị oxi hoá');
Insert into CAUHOI values (3,1,N'Sự phá huỷ kim loại hoặc hợp kim do tác dụng hóa học của môi trường xung quanh gọi là',N'Sự ăn mòn hóa học');
Insert into CAUHOI values (3,1,N'Sắt không bị ăn mòn điện hoá khi tiếp xúc với kim loại nào sau đây trong không khí',N'Zn');
Insert into CAUHOI values (3,2,N'Kim loại M phản ứng với oxi để tạo thành oxit. Khối lượng oxi đã phản ứng bằng 40% khối lượng kim loại đã dùng. Kim loại M là',N'Ca');
Insert into CAUHOI values (3,2,N'Độ âm điện của các nguyên tố: Na, Mg, Al, Si. Xếp theo chiều tăng dần là',N'Na < Mg < Al < Si');
Insert into CAUHOI values (3,2,N'Khi thuỷ phân saccarozo, sản phẩm thu được là',N'glucozo và fructozo');
Insert into CAUHOI values (3,2,N'Có thể phân biệt xenlulozơ với tinh bột nhờ phản ứng',N'với dung dịch iot');
Insert into CAUHOI values (3,2,N'Quá trình kết hợp nhiều phân tử nhỏ (monome) thành phân tử lớn (polime) đồng thời giải phóng những phân tử nhỏ khác (thí dụ H2O) được gọi là phản ứng',N'trùng ngưng');
Insert into CAUHOI values (3,3,N'Polime nào sau đây thuộc loại polime thiên nhiên',N'tinh bột');
Insert into CAUHOI values (3,3,N'Poli(etylen terephtalat) được điều chế bằng phản ứng trùng ngưng giữa axit terephtalic với chất nào saụ đây',N'etylen glicol');
Insert into CAUHOI values (3,3,N'Polime có công thức : (CH2-CH(CH3) )nlà sản phẩm của quá trình trùng hợp monome nào sau đây',N'propilen');
Insert into CAUHOI values (3,3,N'Polime nào dưới đây có cùng cấu trúc mạch polime với nhựa bakelit',N'cao su lưu hoá');
Insert into CAUHOI values (3,3,N'Cho các polime : polietilen, xenlulozơ, polipeptit, tinh bột, nilon-6, nilon-6,6, polibutađien. số polime tổng hợp trong dãy là',N'4');
Insert into CAUHOI values (3,4,N'Cho 1 ml ancol etylic, 1 ml axit axetic và 1 giọt axit sunfuric đặc vào ống nghiệm. Lắc đều và đun nhẹ trên ngọn lửa đèn cồn, sau đó làm lạnh rồi thêm vào ống nghiệm 2 ml dung dịch NaCl bão hoà. Hiện tượng quan sát được là',N'dung dịch phân thành 2 lớp');
Insert into CAUHOI values (3,4,N'Cho 5 giọt CuSO4 5% và 1 ml dung dịch NaOH 10% vào ống nghiệm, lắc nhẹ. Gạn bỏ lóp dung dịch, sau đó thêm vào 2 ml glucozơ 1% lắc nhẹ. Hiện tượng quan sát được là',N'Cu(OH)2 tan tạo dung dịch, màu xanh');
Insert into CAUHOI values (3,4,N'Một loại nước cứng tạm thời chứa ion Ca2+. Cô cạn 100 ml dung dịch nước cứng này thu được 156,8 ml CO2 (đktc). Để loại bỏ tính cứng tạm thời của 1 lít nước cứng này cần dùng tối thiếu số ml dung dịch NaOH 0,1M là',N'140 ml');
Insert into CAUHOI values (3,4,N'Hòa tan hoàn toàn 8,94 gam hỗn hợp gồm Na, K và Ba vào nước thu được dung dịch X và 2,688 lit khí H2 (đktc) . Dung dịch Y gồm HCl và H2SO4 có tỉ lệ mol tương ứng: 4 : 1. Trung hòa dung dịch X bởi dung dịch Y, tổng khối lượng các muối được tạo ra là',N'18,46');
Insert into CAUHOI values (3,4,N'Tính khử của các nguyên tử Na, K, Al, Mg được xếp theo thứ tự tăng dần là',N'Al, Mg, Na, K');

Insert into CAUHOI values (4,1,N'Many desert plants develop their long and shallow root system._________, they can collect much water as much as possible.',N'Therefore');
Insert into CAUHOI values (4,1,N'Deserts often include _________ and rocky surface.',N'Sand');
Insert into CAUHOI values (4,1,N'We go to school every day per week____________ Sundays.',N'except');
Insert into CAUHOI values (4,1,N' ___________ a desert requires a lot of careful preparation and survival skills.',N'Exploring');
Insert into CAUHOI values (4,1,N'You have no choice __________ work hard to make your parents happy.',N'but');
Insert into CAUHOI values (4,2,N'____________ other students, he goes to school five days per week.',N'Like');
Insert into CAUHOI values (4,2,N'Newcomers find it difficult_______ a new environment when studying abroad',N'to adapt to');
Insert into CAUHOI values (4,2,N'_____________ drive to fast. You will be fined.',N'Don’t');
Insert into CAUHOI values (4,2,N'The Sahara is the largest hot desert in the world______ it isn’t the largest one in the world.',N'but');
Insert into CAUHOI values (4,2,N'It is raining heavily_______ we can’t go out for walking.',N'so');
Insert into CAUHOI values (4,3,N'The weather is so cold.________, we still continue our exploration of this beautiful place.',N'However');
Insert into CAUHOI values (4,3,N'I missed the lessons yesterday so I have to___________ on work.',N'catch up');
Insert into CAUHOI values (4,3,N'Teenagers can’t live ___________ a smart phone.',N'without');
Insert into CAUHOI values (4,3,N'I went to a food stall to buy some sandwiches for breakfast________ it didn’t have it.',N'but');
Insert into CAUHOI values (4,3,N'________ Simpson Desert of_______ Australia is the largest desert of the country.',N'The/ Ø');
Insert into CAUHOI values (4,4,N'It is pointed out in the passage that the increase in the world population ______',N'is expected to continue even faster until 2050');
Insert into CAUHOI values (4,4,N'It has been forecast that, by the middle of the twenty-first century _____.',N'the world population will be stabilized at around 10 to 15 billion');
Insert into CAUHOI values (4,4,N'When being interviewed, you should concentrate on what the interviewer is saying orasking you.',N'pay all attention to');
Insert into CAUHOI values (4,4,N'He was so insubordinate that he lost his job within a week',N'obedient');
Insert into CAUHOI values (4,4,N'The children ______ to bed before their parents came home from work.',N'had all gone');

insert into DETHI values (1,1,1,1,15,N'Kiểm tra 15 phút học kỳ 1 năm học 2021-2022','2021-12-03',5);
insert into DETHI values (1,1,1,1,60,N'Kiểm tra 1 tiết học kỳ 1 năm học 2021-2022','2021-12-04',5);
insert into DETHI values (1,1,1,1,60,N'Thi học kỳ 1 năm học 2021-2022','2021-12-05',5);

insert into DETHI values (2,2,1,2,15,N'Kiểm tra 15 phút học kỳ 2 năm học 2021-2022','2022-04-06',5);
insert into DETHI values (2,2,1,2,60,N'Kiểm tra 1 tiết học kỳ 2 năm học 2021-2022','2022-05-07',5);
insert into DETHI values (2,2,1,2,60,N'Thi học kỳ 2 năm học 2021-2022','2022-06-08',5);

insert into DETHI values (2,1,2,2,15,N'Kiểm tra 15 phút học kỳ 1 năm học 2022-2023','2022-10-04',5);
insert into DETHI values (1,1,2,1,60,N'Kiểm tra 1 tiết học kỳ 1 năm học 2022-2023','2022-11-08',5);
insert into DETHI values (3,1,2,3,60,N'Thi học kỳ 1 năm học 2022-2023','2022-12-22',5);

insert into DETHI values (3,2,2,3,15,N'Kiểm tra 15 phút học kỳ 1 năm học 2022-2023','2023-03-12',5);
insert into DETHI values (2,2,2,2,60,N'Kiểm tra 1 tiết học kỳ 1 năm học 2022-2023','2023-04-19',5);
insert into DETHI values (1,2,2,1,60,N'Thi học kỳ 2 năm học 2022-2023','2023-06-26',5);

insert into DETHI values (1,1,1,4,15,N'Kiểm tra 15 phút học kỳ 1 năm học 2021-2022','2021-09-15',5);
insert into DETHI values (1,2,1,4,15,N'Kiểm tra 15 phút học kỳ 2 năm học 2021-2022','2022-04-06',5);
insert into DETHI values (1,1,2,4,15,N'Kiểm tra 15 phút học kỳ 1 năm học 2022-2023','2022-09-20',5);
insert into DETHI values (1,2,2,4,15,N'Kiểm tra 15 phút học kỳ 2 năm học 2022-2023','2023-05-01',5);


insert into CT_DETHI values (1,1,2.5);
insert into CT_DETHI values (1,2,3.5);
insert into CT_DETHI values (1,3,1);
insert into CT_DETHI values (1,4,2);
insert into CT_DETHI values (1,5,1);


insert into CT_DETHI values (2,20,1);
insert into CT_DETHI values (2,19,2);
insert into CT_DETHI values (2,18,2);
insert into CT_DETHI values (2,17,1.5);
insert into CT_DETHI values (2,16,3.5);


insert into CT_DETHI values (3,14,2.5);
insert into CT_DETHI values (3,13,1);
insert into CT_DETHI values (3,12,3);
insert into CT_DETHI values (3,11,1);
insert into CT_DETHI values (3,10,2.5);


insert into CT_DETHI values (4,21,3.5);
insert into CT_DETHI values (4,22,0.5);
insert into CT_DETHI values (4,23,0.5);
insert into CT_DETHI values (4,24,3.5);
insert into CT_DETHI values (4,25,2);


insert into CT_DETHI values (5,40,2.5);
insert into CT_DETHI values (5,39,3.5);
insert into CT_DETHI values (5,38,1.5);
insert into CT_DETHI values (5,37,0.5);
insert into CT_DETHI values (5,36,2);


insert into CT_DETHI values (6,34,2.5);
insert into CT_DETHI values (6,33,1.5);
insert into CT_DETHI values (6,32,1.5);
insert into CT_DETHI values (6,31,3.5);
insert into CT_DETHI values (6,30,1);

insert into CT_DETHI values (7,23,1);
insert into CT_DETHI values (7,35,2);
insert into CT_DETHI values (7,27,1);
insert into CT_DETHI values (7,21,5);
insert into CT_DETHI values (7,28,1);

insert into CT_DETHI values (8,19,1.5);
insert into CT_DETHI values (8,1,1.5);
insert into CT_DETHI values (8,9,4);
insert into CT_DETHI values (8,8,2);
insert into CT_DETHI values (8,15,1);

insert into CT_DETHI values (9,47,2);
insert into CT_DETHI values (9,57,3.5);
insert into CT_DETHI values (9,60,1);
insert into CT_DETHI values (9,41,1.5);
insert into CT_DETHI values (9,51,2);

insert into CT_DETHI values (10,43,2.5);
insert into CT_DETHI values (10,49,1);
insert into CT_DETHI values (10,57,1);
insert into CT_DETHI values (10,52,3.5);
insert into CT_DETHI values (10,46,2);

insert into CT_DETHI values (11,29,3);
insert into CT_DETHI values (11,31,2);
insert into CT_DETHI values (11,21,3);
insert into CT_DETHI values (11,27,0.5);
insert into CT_DETHI values (11,35,1.5);

insert into CT_DETHI values (12,9,1);
insert into CT_DETHI values (12,6,3);
insert into CT_DETHI values (12,19,1);
insert into CT_DETHI values (12,13,3);
insert into CT_DETHI values (12,15,2);

Insert into CT_DETHI values (13,61,2);
Insert into CT_DETHI values (13,71,3);
Insert into CT_DETHI values (13,72,1);
Insert into CT_DETHI values (13,76,1);
Insert into CT_DETHI values (13,62,3);

Insert into CT_DETHI values (14,69,2.5);
Insert into CT_DETHI values (14,61,1.5);
Insert into CT_DETHI values (14,79,1);
Insert into CT_DETHI values (14,80,2);
Insert into CT_DETHI values (14,71,3);

Insert into CT_DETHI values (15,76,1);
Insert into CT_DETHI values (15,65,1);
Insert into CT_DETHI values (15,67,3);
Insert into CT_DETHI values (15,63,1);
Insert into CT_DETHI values (15,73,4);

Insert into CT_DETHI values (16,71,2);
Insert into CT_DETHI values (16,66,2);
Insert into CT_DETHI values (16,77,3);
Insert into CT_DETHI values (16,72,2);
Insert into CT_DETHI values (16,63,1);


insert into LOPHOC Values (N'lớp 1');
insert into LOPHOC Values (N'lớp 2');
insert into LOPHOC values (N'lớp 3');

insert into SINHVIEN values (N'Nguyễn Văn A');
insert into SINHVIEN values (N'Nguyễn Văn B');
insert into SINHVIEN values (N'Nguyễn Văn C');
insert into SINHVIEN values (N'Nguyễn Văn D');
insert into SINHVIEN values (N'Nguyễn Văn E');
insert into SINHVIEN values (N'Nguyễn Văn F');
insert into SINHVIEN values (N'Nguyễn Văn G');
insert into SINHVIEN values (N'Nguyễn Văn H');
insert into SINHVIEN values (N'Nguyễn Văn I');
insert into SINHVIEN values (N'Nguyễn Văn J');
insert into SINHVIEN values (N'Nguyễn Văn K');
insert into SINHVIEN values (N'Nguyễn Văn M');
insert into SINHVIEN values (N'Nguyễn Văn N');
insert into SINHVIEN values (N'Nguyễn Văn O');
insert into SINHVIEN values (N'Nguyễn Văn P');
insert into SINHVIEN values (N'Nguyễn Văn Q');
insert into SINHVIEN values (N'Nguyễn Văn R');
insert into SINHVIEN values (N'Nguyễn Văn S');


insert into CT_LOPHOC values (1,1);
insert into CT_LOPHOC values (1,2);
insert into CT_LOPHOC values (1,3);
insert into CT_LOPHOC values (1,4);
insert into CT_LOPHOC values (1,5);
insert into CT_LOPHOC values (1,6);
insert into CT_LOPHOC values (2,7);
insert into CT_LOPHOC values (2,8);
insert into CT_LOPHOC values (2,9);
insert into CT_LOPHOC values (2,10);
insert into CT_LOPHOC values (2,11);
insert into CT_LOPHOC values (2,12);
insert into CT_LOPHOC values (3,13);
insert into CT_LOPHOC values (3,14);
insert into CT_LOPHOC values (3,15);
insert into CT_LOPHOC values (3,16);
insert into CT_LOPHOC values (3,17);
insert into CT_LOPHOC values (3,18);



insert into KETQUACHAMTHI values (1,1,1,6);
insert into KETQUACHAMTHI values (4,1,2,6);
insert into KETQUACHAMTHI values (2,2,1,6);
insert into KETQUACHAMTHI values (5,2,2,6);
insert into KETQUACHAMTHI values (7,3,2,6);
insert into KETQUACHAMTHI values (9,3,3,6);
insert into KETQUACHAMTHI values (12,3,1,6);
insert into KETQUACHAMTHI values (8,3,1,6);
insert into KETQUACHAMTHI values (13,3,1,6);
insert into KETQUACHAMTHI values (14,3,1,6);
insert into KETQUACHAMTHI values (15,3,1,6);
insert into KETQUACHAMTHI values (16,3,1,6);

insert into CT_KETQUACHAMTHI values (1,1,9,N'chín',N'tư duy tốt');
insert into CT_KETQUACHAMTHI values (1,2,9.5,N'chín chấm năm',N'giỏi');
insert into CT_KETQUACHAMTHI values (1,3,8,N'tám',N'cố gắng tốt hơn lần sau');
insert into CT_KETQUACHAMTHI values (1,4,10,N'mười',N'Xuất sắc');
insert into CT_KETQUACHAMTHI values (1,5,8.5,N'tám chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (1,6,7,N'bảy',N'cần kỹ càng hơn');

insert into CT_KETQUACHAMTHI values (2,1,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (2,2,9,N'chín',N'tốt');
insert into CT_KETQUACHAMTHI values (2,3,9.5,N'chín chấm năm',N'giỏi');
insert into CT_KETQUACHAMTHI values (2,4,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (2,5,8,N'tám',N'học lại công thức');
insert into CT_KETQUACHAMTHI values (2,6,10,N'mười',N'giỏi');

insert into CT_KETQUACHAMTHI values (3,7,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (3,8,9.5,N'chín chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (3,9,7.5,N'bảy chấm năm',N'cố gắng trong lần tới');
insert into CT_KETQUACHAMTHI values (3,10,8,N'tám',N'tính toán kỹ hơn');
insert into CT_KETQUACHAMTHI values (3,11,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (3,12,9,N'chín',N'tốt nhưng cần kỹ hơn');

insert into CT_KETQUACHAMTHI values (4,7,6,N'sáu',N'học lại tích phân và hàm phân phối xác suất');
insert into CT_KETQUACHAMTHI values (4,8,9.5,N'chín chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (4,9,9.75,N'chín chấm bảy lăm',N'giỏi');
insert into CT_KETQUACHAMTHI values (4,10,8.5,N'tám chấm năm',N'tính toán kỹ hơn');
insert into CT_KETQUACHAMTHI values (4,11,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (4,12,7.25,N'bảy chấm hai lăm',N'học lại công thức');

insert into CT_KETQUACHAMTHI values (5,13,6,N'sáu',N'học lại tích phân và hàm phân phối xác suất');
insert into CT_KETQUACHAMTHI values (5,14,9.5,N'chín chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (5,15,9.75,N'chín chấm bảy lăm',N'giỏi');
insert into CT_KETQUACHAMTHI values (5,16,8.5,N'tám chấm năm',N'tính toán kỹ hơn');
insert into CT_KETQUACHAMTHI values (5,17,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (5,18,7.25,N'bảy chấm hai lăm',N'học lại phương trình');

insert into CT_KETQUACHAMTHI values (6,13,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (6,14,9.5,N'chín chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (6,15,7.5,N'bảy chấm năm',N'cố gắng trong lần tới, học thuộc bảng tuần hoàn hóa học');
insert into CT_KETQUACHAMTHI values (6,16,8,N'tám',N'tính toán kỹ hơn');
insert into CT_KETQUACHAMTHI values (6,17,10,N'mười',N'giỏi');
insert into CT_KETQUACHAMTHI values (6,18,9,N'chín',N'tốt nhưng cần kỹ hơn');

insert into CT_KETQUACHAMTHI values (7,13,9,N'chín',N'tư duy tốt');
insert into CT_KETQUACHAMTHI values (7,14,9.5,N'chín chấm năm',N'giỏi');
insert into CT_KETQUACHAMTHI values (7,15,8,N'tám',N'cố gắng tốt hơn lần sau');
insert into CT_KETQUACHAMTHI values (7,16,10,N'mười',N'Xuất sắc');
insert into CT_KETQUACHAMTHI values (7,17,8.5,N'tám chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (7,18,7,N'bảy',N'cần kỹ hơn');

insert into CT_KETQUACHAMTHI values (8,13,10,N'mười',N'xuất sắc');
insert into CT_KETQUACHAMTHI values (8,14,7.5,N'bảy chấm năm',N'Học lại cách dạng vận dụng cao');
insert into CT_KETQUACHAMTHI values (8,15,8,N'tám',N'cố gắng tốt hơn lần sau');
insert into CT_KETQUACHAMTHI values (8,16,9.5,N'chín chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (8,17,8.5,N'tám chấm năm',N'kỹ càng hơn trong sóng cơ');
insert into CT_KETQUACHAMTHI values (8,18,7.5,N'bảy chấm năm',N'cẩn thận hơn, ôn lại điện xoay chiều');

insert into CT_KETQUACHAMTHI values (9,13,10,N'xuất sắc',N'tư duy tốt');
insert into CT_KETQUACHAMTHI values (9,14,7,N'bảy',N'học lại quá khứ đơn và từ vựng');
insert into CT_KETQUACHAMTHI values (9,15,8,N'tám',N'cố gắng tốt hơn lần sau');
insert into CT_KETQUACHAMTHI values (9,16,10,N'mười',N'Xuất sắc');
insert into CT_KETQUACHAMTHI values (9,17,8,N'tám',N'chú ý từ loại');
insert into CT_KETQUACHAMTHI values (9,18,7.5,N'bảy chấm năm',N'học lại từ vựng chương 3');

insert into CT_KETQUACHAMTHI values (10,13,9,N'chín',N'tư duy tốt');
insert into CT_KETQUACHAMTHI values (10,14,9,N'chín',N'tốt nhưng cần kỹ càng hơn');
insert into CT_KETQUACHAMTHI values (10,15,10,N'mười',N'excellent');
insert into CT_KETQUACHAMTHI values (10,16,10,N'mười',N'good');
insert into CT_KETQUACHAMTHI values (10,17,8.5,N'tám chấm năm',N'cần suy luận tốt hơn');
insert into CT_KETQUACHAMTHI values (10,18,7.5,N'bảy chấm năm',N'Học lại thì hoàn thành');

insert into CT_KETQUACHAMTHI values (11,13,7,N'bảy',N'Học lại từ vựng, động từ to be');
insert into CT_KETQUACHAMTHI values (11,14,9.5,N'chín chấm năm',N'giỏi');
insert into CT_KETQUACHAMTHI values (11,15,8.5,N'tám chấm năm',N'cố gắng tốt hơn lần sau');
insert into CT_KETQUACHAMTHI values (11,16,10,N'mười',N'Nice');
insert into CT_KETQUACHAMTHI values (11,17,6,N'sáu',N' bad, cần học lại từ vựng và các thì trong câu');
insert into CT_KETQUACHAMTHI values (11,18,8,N'bảy',N'cần kỹ hơn');

insert into CT_KETQUACHAMTHI values (12,13,8.5,N'tám chấm năm',N'cố gắng lần sau');
insert into CT_KETQUACHAMTHI values (12,14,9.5,N'chín chấm năm',N'giỏi');
insert into CT_KETQUACHAMTHI values (12,15,8,N'tám',N'cố gắng tốt hơn lần sau');
insert into CT_KETQUACHAMTHI values (12,16,7,N'bảy',N'ẩu, cần học lại từ vựng');
insert into CT_KETQUACHAMTHI values (12,17,8.5,N'tám chấm năm',N'tốt');
insert into CT_KETQUACHAMTHI values (12,18,10,N'mười',N'very good');

insert into THAMSO values ('SoCauToiDa', 5)
insert into THAMSO values ('DiemSoCauToiDa', 10)
insert into THAMSO values ('DiemSoCauToiThieu', 1)
insert into THAMSO values ('TongDiem', 10)
insert into THAMSO values ('ThoiLuongThiToiDa', 180)
insert into THAMSO values ('ThoiLuongThiToiThieu', 30)
insert into THAMSO values ('DiemSoToiDa', 10)
insert into THAMSO values ('DiemSoToiThieu', 0)

insert into ADMIN values ('manh@uit', '123')
