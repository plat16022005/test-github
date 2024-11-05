class GiaoDich:
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong):
        self.ma_gd = ma_gd
        self.ngay_gd = ngay_gd
        self.don_gia = don_gia
        self.so_luong = so_luong
    def thanh_tien(self):
        return self.so_luong * self.don_gia
    def hien_thi(self):
        print(f"Mã giao dịch: {self.ma_gd}")
        print(f"Ngày giao dịch: {self.ngay_gd}")
        print(f"Đơn giá: {self.don_gia}")
        print(f"Số lượng: {self.so_luong}")
class GiaoDichVang(GiaoDich):
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong, loai_vang):
        super().__init__(ma_gd, ngay_gd, don_gia, so_luong)
        self.loai_vang = loai_vang
    def thanh_tien(self):
        return self.so_luong * self.don_gia
    def hien_thi(self):
        super().hien_thi()
        print(f"Loại vàng: {self.loai_vang}")
        print(f"Thành tiền: {self.thanh_tien()}")
class GiaoDichTienTe(GiaoDich):
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong, loai_tien, loai_gd):
        super().__init__(ma_gd, ngay_gd, don_gia, so_luong)
        self.loai_tien = loai_tien 
        self.loai_gd = loai_gd
    def thanh_tien(self):
        if self.loai_gd == 'mua':
            return self.so_luong * self.don_gia
        elif self.loai_gd == 'ban':
            return self.so_luong * self.don_gia * 1.05
    def hien_thi(self):
        super().hien_thi()
        print(f"Loại tiền tệ: {self.loai_tien}")
        print(f"Loại giao dịch: {self.loai_gd}")
        print(f"Thành tiền: {self.thanh_tien()}")
def nhap_giao_dich_vang():
    ma_gd = input("Nhập mã giao dịch: ")
    ngay_gd = input("Nhập ngày giao dịch (dd/mm/yyyy): ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = float(input("Nhập số lượng: "))
    loai_vang = input("Nhập loại vàng (18k, 24k, 9999): ")
    return GiaoDichVang(ma_gd, ngay_gd, don_gia, so_luong, loai_vang)
def nhap_giao_dich_tien_te():
    ma_gd = input("Nhập mã giao dịch: ")
    ngay_gd = input("Nhập ngày giao dịch (dd/mm/yyyy): ")
    don_gia = float(input("Nhập tỷ giá (đơn giá): "))
    so_luong = float(input("Nhập số lượng: "))
    loai_tien = input("Nhập loại tiền tệ (USD, EUR, AUD): ")
    loai_gd = input("Nhập loại giao dịch (mua/bán): ")
    return GiaoDichTienTe(ma_gd, ngay_gd, don_gia, so_luong, loai_tien, loai_gd)
def hien_thi_danh_sach_giao_dich(ds_giao_dich):
    for gd in ds_giao_dich:
        gd.hien_thi()
        print("-" * 30)
def tinh_tong_so_luong(ds_giao_dich):
    tong_vang = 0
    tong_tien_te = 0
    for gd in ds_giao_dich:
        if isinstance(gd, GiaoDichVang):
            tong_vang += gd.so_luong
        elif isinstance(gd, GiaoDichTienTe):
            tong_tien_te += gd.so_luong
    print(f"Tổng số lượng vàng: {tong_vang}")
    print(f"Tổng số lượng tiền tệ: {tong_tien_te}")
def tinh_tong_thanh_tien(ds_giao_dich):
    tong_vang = 0
    tong_tien_te = 0
    for gd in ds_giao_dich:
        if isinstance(gd, GiaoDichVang):
            tong_vang += gd.thanh_tien()
        elif isinstance(gd, GiaoDichTienTe):
            tong_tien_te += gd.thanh_tien()
    print(f"Tổng thành tiền giao dịch vàng: {tong_vang}")
    print(f"Tổng thành tiền giao dịch tiền tệ: {tong_tien_te}")
ds_giao_dich = []
while True:
    loai_gd = input("Bạn muốn nhập giao dịch loại nào? (1: Vàng, 2: Tiền tệ, 0: Thoát): ")
    if loai_gd == "1":
        gd = nhap_giao_dich_vang()
        ds_giao_dich.append(gd)
    elif loai_gd == "2":
        gd = nhap_giao_dich_tien_te()
        ds_giao_dich.append(gd)
    elif loai_gd == "0":
        break
hien_thi_danh_sach_giao_dich(ds_giao_dich)
tinh_tong_so_luong(ds_giao_dich)
tinh_tong_thanh_tien(ds_giao_dich)