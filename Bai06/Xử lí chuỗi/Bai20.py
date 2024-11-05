def dem_so_luong(a):
    so = int()
    viethoa = int()
    vietthuong = int()
    kitu = int()
    for i in a:
        if "0" <= i and i <= "9":
            so += 1
        elif "A" <= i and i <= "Z":
            viethoa += 1
        elif "a" <= i and i <= "z":
            vietthuong += 1
        else:
            kitu += 1
    return so, viethoa, vietthuong, kitu
def main():
    a = str(input("Nhập chuỗi: "))
    so,viethoa,vietthuong,kitu = dem_so_luong(a)
    print("Số lượng kí tự số là: {0}; Kí tự viết hoa là: {1}; Kí tự viết thường là: {2}; Kí tự khác là: {3}".format(so,viethoa,vietthuong,kitu))
main()