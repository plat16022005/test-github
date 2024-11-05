import math
class Circle:
    def __init__(self, r):
        self.r = float(r)
    def ChuVi(self):
        return 2*math.pi*self.r
    def DienTich(self):
        return 2*math.pi*self.r**2
    def Show(self):
        print("Hình tròn bán kính là: ", self.r, " Với chu vi và diện tích lần lượt là: ", self.ChuVi(), self.DienTich())
a = Circle(3)
a.Show()