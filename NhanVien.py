class DiaChi:
    def __init__(self,sonha,tenduong,tenquan,thanhpho):
        self.sonha=sonha
        self.tenduong=tenduong
        self.tenquan=tenquan
        self.thanhpho=thanhpho
class NhanVien:
    def __init__(self, hoten, ngaysinh, diachi:DiaChi):
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.diachi = diachi
    def InThongTin(self):
        print("Tên nhân viên: ",self.hoten)
        print("Ngày sinh: ", self.ngaysinh)
        print("Địa chỉ: ", end ="")
        print(self.diachi.sonha,self.diachi.tenduong,self.diachi.tenquan,self.diachi.thanhpho,sep="/ ")
class NhanVienSanXuat(NhanVien):
    def __init__(self, hoten, ngaysinh, diachi,luongcb,sosp):
        super().__init__(hoten, ngaysinh,diachi)
        self.luongcb = luongcb
        self.sosp = sosp
    def InThongTin(self):
        super().InThongTin()
        print("Lương căn bản:", self.luongcb)
        print("Số sản phẩm sản xuất được:", self.sosp)
    def TinhLuong(self):
        return self.luongcb + self.sosp*5000
class NhanVienVanPhong(NhanVien):
    def __init__(self, hoten, ngaysinh, diachi, snlv):
        super().__init__(hoten, ngaysinh, diachi)
        self.snlv = snlv
    def InThongTin(self):
        super().InThongTin()
        print("Số ngày làm việc:",self.snlv)
    def TinhLuong(self):
        return self.snlv*100000
a = NhanVienSanXuat("Phạm Lê Anh Tuấn", "16/02/2005", DiaChi("138","Nguyễn Văn Tiến","Cần Đước","LongAn"),10000,100)
b = NhanVienVanPhong("Trình Văn Lưu", "14/12/2005", DiaChi("1","Nguyễn Văn Ngân","Thủ Đức","Thành phố Hồ Chí Minh"),28)
c = NhanVienSanXuat("Phan Đình Sáng", ".../.../2005", DiaChi("1","Mạc Đĩnh Chi", "Dĩ An", "Bình Dương"),3000,50)
d = NhanVienSanXuat("Trịnh Quốc Công Vinh", ".../.../2005",DiaChi("...","...","Biên Hòa","Đồng Nai"), 5000, 80)
e = NhanVienVanPhong("Trần Minh Thuận", ".../.../...2005",DiaChi("...","...","Biên Hòa","Đồng Nai"), 25)
for i in [a,b,c,d,e]:
    i.InThongTin()
    print("Lương:", i.TinhLuong())
    print()