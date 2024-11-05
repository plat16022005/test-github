import numpy as np
def product(mat_a, mat_b):
    if mat_a.shape[1] == mat_b.shape[0]:
        mat_product = np.dot(mat_a, mat_b)
        print("Tích ma trận:")
        print(mat_product)
    else:
        print("Khong co tich ma tran")
    if mat_a.shape == mat_b.shape:
        hadamard_product = np.multiply(mat_a, mat_b)
        print("Tích Hadamard:")
        print(hadamard_product)
    else:
        print("Khong co tich Hadamard")
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
product(mat_a, mat_b)