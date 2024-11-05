import numpy as np
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
if a >= b:
    print("Giá trị a phải nhỏ hơn giá trị b.")
else:
    random_array = a + (b - a) * np.random.rand(10)
    print("Mảng chứa 10 số thực ngẫu nhiên trong khoảng (a, b):")
    print(random_array)