class Sample():
# (4) phương thức khởi tạo tự động thực thi
    def __init__(self):
        self.a = 1
        self._b = 2 # biến nội bộ (1)
        self.__c = 3 # biến mangling (3)
class SecondClass(Sample): # kế thừa
    def __init__(self):
        super().__init__()
        self.a = "overridden"
        self._b = "overridden"
        self.__c = "overridden"
obj2 = SecondClass()
print(obj2.a) # … ?
print(obj2._b) # … ?
print(obj2.__c) # … ?