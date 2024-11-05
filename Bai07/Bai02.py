class TamGiac:
    def __init__(self,a,b,c,mau):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.mau = mau
    def ChuVi(self):
        return self.a + self.b + self.c
    def DienTich(self):
        return (self.ChuVi()/2*(self.ChuVi()/2-self.a)*(self.ChuVi()/2-self.b)*(self.ChuVi()/2-self.c))**(1/2)
    def Show(self):
        print("Tam giác này có 3 cạnh lần lượt là: ", self.a, self.b, self.c)
        print("Màu sắc của nó là: ", self.mau)
        print("Có Chu vi và diện tích lần lượt là: ",self.ChuVi(), self.DienTich())
        if (self.a == self.b == self.c):
            print("Đây là tam giác đều")
        elif self.a**2 + self.b**2 == max(self.a,self.b,self.c)**2 or self.c**2 + self.b**2 == max(self.a,self.b,self.c)**2 or self.a**2 + self.c**2 == max(self.a,self.b,self.c)**2:
            if (self.a == self.b != self.c) or (self.a != self.b == self.c) or (self.a == self.c != self.b):
                print("Đây là tam giác vuông cân")
            else:
                print("Đây là tam giác vuông")
        elif (self.a == self.b != self.c) or (self.a != self.b == self.c) or (self.a == self.c != self.b):
            print("Đây là tam giác cân")
        else:
            print("Đây là tam giác thường")
a = TamGiac(2**(1/2),2**(1/2),2, "Đỏ")
a.Show()