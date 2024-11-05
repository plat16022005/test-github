import numpy as np
import random
print("Mảng Numpy được tạo ngẫu nhiên là:")
random_array = np.random.randint(-100,101,size=random.randint(10,31))
print(random_array)
duong_array = []
for i in random_array:
    if i > 0:
        duong_array.append(i)
print("Mảng số dương được tạo từ Numpy Array một chiều trên là:")
print(list(map(int, duong_array)))