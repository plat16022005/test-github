def TinhTrungVi(a,b,c):
    return sorted([a,b,c])[1]
def main():
    a = float(input("Nhập giá trị thứ nhất: "))
    b = float(input("Nhập giá trị thứ hai: "))
    c = float(input("Nhập giá trị thứ ba: "))
    TrungVi = TinhTrungVi(a,b,c)
    print("Trung vị của 3 điểm là: ", TrungVi)
main()