import numpy as np
def replace_col(mat, col_ind):
    mat[:, col_ind] = 1
    return mat
mat = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
col_ind = 1
new_mat = replace_col(mat, col_ind)
print("Ma trận sau khi thay thế cột:")
print(new_mat)