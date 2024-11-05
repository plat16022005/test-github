def tim_so_luong_tu(a,s):
    soluong = int()
    for i in a:
        if i == s:
            soluong += 1
    return soluong
def main():
    a = str(input("Nhập chuỗi: "))
    s = str(input("Nhập ký tự muốn tìm: "))
    soluong = tim_so_luong_tu(a,s)
    print("Số lượng ký tự '{0}' mà bạn muốn tìm là: {1}".format(s,soluong))
main()