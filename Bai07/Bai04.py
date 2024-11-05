class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def HienThi(self):
        print("({0}, {1})".format(self.x,self.y))
    def TinhTien(self,x,y=0):
        self.x+=x
        self.y+=y
    def KhoangCach(self, d=None):
        if d==None:
            return (self.x**2+self.y**2)**(1/2)
        else:
            return ((self.x-d.x)**2+(self.y-d.y)**2)**(1/2)
a = Point(3,5)
a.HienThi()
a.TinhTien(9)
a.HienThi()
a.TinhTien(2,5)
a.HienThi()
print("Khoảng cách giữa điểm a với gốc tọa độ là: ", a.KhoangCach())
d = Point(2,6)
print("Khoảng cách giữa điểm a({0}, {1}) và điểm d({2}, {3}) là: ".format(a.x,a.y,d.x,d.y), a.KhoangCach(d))