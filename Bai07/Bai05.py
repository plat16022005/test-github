import math
class Circle:
    def __init__(self, r):
        self.r = r
    def ChuVi(self):
        return 2*math.pi*self.r
    def DienTich(self):
        return 2*math.pi*self.r**2
class HinhChuNhat:
    def __init__(self,a,b):
        self.a = float(a)
        self.b = float(b)
    def ChuVi(self):
        return (self.a + self.b)*2
    def DienTich(self):
        return self.a*self.b
class TamGiac:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def ChuVi(self):
        return self.a + self.b + self.c
    def DienTich(self):
        return (self.ChuVi()/2*(self.ChuVi()/2-self.a)*(self.ChuVi()/2-self.b)*(self.ChuVi()/2-self.c))**(1/2)
class ChuViVaDienTich:
    def __init__(self,a=None):
        self.a=a
    def HienThi(self):
        if self.a is not None:
            print("Chu vi và diện tích hình bạn vừa cung cấp là: ",self.a.ChuVi(),";",self.a.DienTich()) 
a = Circle(3)
b = HinhChuNhat(3,4)
c = TamGiac(3,4,5)
CSa = ChuViVaDienTich(a)
CSa.HienThi()
CSb = ChuViVaDienTich(b)
CSb.HienThi()
CSc = ChuViVaDienTich(c)   
CSc.HienThi()