def kt_can_cuoc(a):
    if len(a) != 12:
        return False
    for i in a:
        if not("0" <= i and i <= "9"):
            return False
    if a[0] != "0":
        return False
    if a[3] != "1" and a[3] != "0":
        return False
    return True
dist = {
    1: "An Giang",
    2: "Bà Rịa - Vũng Tàu",
    3: "Bắc Giang",
    4: "Bắc Kạn",
    5: "Bạc Liêu",
    6: "Bắc Ninh",
    7: "Bến Tre",
    8: "Bình Định",
    9: "Bình Dương",
    10: "Bình Phước",
    11: "Bình Thuận",
    12: "Cà Mau",
    13: "Cần Thơ",
    14: "Cao Bằng",
    15: "Đà Nẵng",
    16: "Đắk Lắk",
    17: "Đắk Nông",
    18: "Điện Biên",
    19: "Đồng Nai",
    20: "Đồng Tháp",
    21: "Gia Lai",
    22: "Hà Giang",
    23: "Hà Nam",
    24: "Hà Nội",
    25: "Hà Tĩnh",
    26: "Hải Dương",
    27: "Hải Phòng",
    28: "Hậu Giang",
    29: "Hòa Bình",
    30: "Hưng Yên",
    31: "Khánh Hòa",
    32: "Kiên Giang",
    33: "Kon Tum",
    34: "Lai Châu",
    35: "Lâm Đồng",
    36: "Lạng Sơn",
    37: "Lào Cai",
    38: "Long An",
    39: "Nam Định",
    40: "Nghệ An",
    41: "Ninh Bình",
    42: "Ninh Thuận",
    43: "Phú Thọ",
    44: "Phú Yên",
    45: "Quảng Bình",
    46: "Quảng Nam",
    47: "Quảng Ngãi",
    48: "Quảng Ninh",
    49: "Quảng Trị",
    50: "Sóc Trăng",
    51: "Sơn La",
    52: "Tây Ninh",
    53: "Thái Bình",
    54: "Thái Nguyên",
    55: "Thanh Hóa",
    56: "Thừa Thiên Huế",
    57: "Tiền Giang",
    58: "TP. Hồ Chí Minh",
    59: "Trà Vinh",
    60: "Tuyên Quang",
    61: "Vĩnh Long",
    62: "Vĩnh Phúc",
    63: "Yên Bái"
}
def tinh_gt_namsinh(a):
    ketqua = []
    matinh = int(a[1:3])
    if kt_can_cuoc(a) and 0 <= matinh <= 63:
        ketqua.append(dist.get(matinh))
    if kt_can_cuoc(a):
        if a[3] == "0":
            ketqua.append("Nữ")
        else:
            ketqua.append("Nam")
    if kt_can_cuoc(a):
        if 0 <= int(a[4:6]) <= 24:
            ketqua.append("20" + a[4:6])
        else:
            ketqua.append("19" + a[4:6])
    ketqua.append(a[6:])
    return ketqua
def main():
    cancuoc = input()
    print(tinh_gt_namsinh(cancuoc))
main()