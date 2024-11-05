import numpy as np
import random
random_array = np.random.randint(-100,101,size=random.randint(10,31))
print(random_array)
print("Chỉ mục của số lớn nhất trong mảng 1 chiều vừa tạo ở trên là: ", np.argmax(random_array))