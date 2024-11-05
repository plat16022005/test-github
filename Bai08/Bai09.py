import numpy as np
def broadcast(vec, n):
    return np.tile(vec.reshape(-1, 1), n)
vec = np.array([6, 7])
n = 3
print("Kết quả broadcast:")
print(broadcast(vec, n))