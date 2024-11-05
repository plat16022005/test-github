class ToanHoc:
    def __init__(self, a=[]):
        self.a = a
    def TinhTong(self):
        tong = float()
        for i in self.a:
            tong += i
        return tong
    def TinhTrungBinh(self):
        if len(self.a) != 0:
            return self.TinhTong()/len(self.a)
        else:
            pass
    def TimMax(self):
        if len(self.a) != 0:
            return max(self.a)
        else:
            pass
    def TimMin(self):
        if len(self.a) != 0:
            return min(self.a)
        else:
            pass
    def HienThi(self):
        print("n số là: ", self.a)
        print("Tổng n số là: ", self.TinhTong())
        print("Trung bình n số là: ", self.TinhTrungBinh())
        print("Số lớn nhất trong n số là: ", self.TimMax())
        print("Số bé nhất trong n số là: ", self.TimMin())
b = [9,6,3,1,6,8,0,5,3,1]
a = ToanHoc(b)
a.HienThi()