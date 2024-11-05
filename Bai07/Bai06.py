class MonHoc:
    def __init__(self):
        self.ma = input("Nhập mã môn (Không nhập gì! Nhần Enter để dừng): ")
        if self.ma == "":
            return
        self.ten = input("Nhập tên môn: ")
        self.sotiet = input("Nhập số tiết: ")
        
    def show(self):
        print("+) Mã môn:", self.ma)
        print("+) Tên môn:", self.ten)
        print("+) Số tiết:", self.sotiet)
class HocVien:
    def __init__(self):
        self.cccd = input("Nhập mã CCCD (Không nhập gì! Nhần Enter để dừng): ")
        if self.cccd == "":
            return
        self.ten = input("Nhập tên sinh viên: ")
        self.nam = input("Nhập năm sinh: ")
        self.monhoc = []
        self.soluong = int()
        while(True):
            self.mon = MonHoc()
            if self.mon.ma == "":
                break
            else:
                self.monhoc.append(self.mon)
                self.soluong += 1
    def HienThi(self):
        print("Mã CCCD: ", self.cccd)
        print("Tên sinh viên: ", self.ten)
        print("Năm sinh: ", self.nam)
        print("CÁC MÔN MÀ SINH VIÊN ĐÃ ĐĂNG KÍ LÀ: ")
        dem = int(1)
        for i in self.monhoc:
            print("- Môn thứ {0}: ".format(dem))
            i.show()
            dem += 1
a = []
b = {}
while (True):
    x = HocVien()
    if x.cccd == "":
        break
    else:
        a.append(x)
print("``Danh sách``: ")
for i in a:
    i.HienThi()
print("`` Các sinh viên đăng kí 2 môn trở lên ``: ")
for i in a:
    if i.soluong >= 2:
        print(i.ten)
for i in a:
    for mon in i.monhoc:
        if mon.ten not in b:
            b[mon.ten] = 1
        else:
            b[mon.ten] += 1
print("`` Môn học được đăng kí nhiều nhất ``: ")
if b:
    max_mon = max(b, key=b.get)
    print("`` Môn học được đăng kí nhiều nhất ``: ")
    print(f"Môn: {max_mon}, Số lượng đăng ký: {b[max_mon]}")
else:
    print("Không có môn học nào được đăng ký.")
print("`` Số lượng sinh viên mỗi môn học ``:") 
print(b)