n = int(input("Nhập số lượng học sinh: "))
mydict = {}
thongke = [int(0)]*11
for i in range(n):
    ten = str(input("Nhập tên: "))
    diem = int(input("Nhập điểm: "))
    mydict[ten] = diem
    thongke[diem] += 1
for i in range(len(thongke)):
    if (thongke[i]!=0):
        print("Số lượng học sinh đạt {0} điểm là: ".format(i), thongke[i])