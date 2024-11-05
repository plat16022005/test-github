
def InputMatran(a):
    n = int(input("Nhập số hàng: "))
    m = int(input("Nhập số cột: "))
    for i in range(n):
        a.append([])
        for j in range(m):
            x = int(input())
            a[i].append(x)

# a=InputMatran(a)
# for i in a:
#     print(i)
# Khởi tạo một ma trận ví dụ

# matrix1 = [[1, 2, 3], 
#           [4, 5, 6], 
#           [7, 8, 9]]
# matrix2 = [[9,8,7],
#            [6,5,4],
#            [3,2,1]]
# def CongMatran(a,b):
#     ketqua = []
#     for i in range(len(a)):
#         ketqua.append([])
#         for j in range(len(a[0])):
#             ketqua[i].append(a[i][j]+b[i][j])
#     return ketqua
# def NhanMatran(a,b):
#     ketqua=[]
#     for i in range(len(a)):
#         ketqua.append([])
#         for j in range(len(b[0])):
#             sum = 0
#             for k in range(len(b)):
#                 sum += (a[i][k]*b[k][j])
#             ketqua[i].append(sum)
#     return ketqua
# def Hoanvi(a):
#     ketqua = []
#     for i in range(len(a[0])):
#         ketqua.append([])
#         for j in range(len(a)):
#             ketqua[i].append(a[j][i])
#     return ketqua
def PrintMatran(result):
    print("Ma trận là:")
    for row in result:
        print(row, end=" ")
        print()  # Xuống dòng sau khi in xong một hàng
# result = NhanMatran(matrix1,matrix2)
# # In ma trận
# PrintMatran(result)
# resultT = Hoanvi(result)
# PrintMatran(resultT)
# PrintMatran(NhanMatran(result,resultT))
# PrintMatran(NhanMatran(resultT,result))

# arr = []
# result = []
# n = int(input("Nhập số lượng phần tử trong mảng: "))
# for i in range(n):
#     x = int(input())
#     arr.append(x)
# k = int(input("Nhập giá trị k: "))
# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
#         if arr[i]+arr[j]==k:
#             result.append((arr[i],arr[j]))
# for i in result:
#     print(i)

# def Collazt(n=int()):
#     ketqua = []
#     ketqua.append(n)
#     while(n!=1):
#         if (n%2==0):
#             n=int(n/2)
#             ketqua.append(n)
#         else:
#             n = int(3*n + 1)
#             ketqua.append(n)
#     for i in ketqua:
#         print(i, end = " ")
#     print()
# n = int(input())
# for i in range(1, n+1):
#     Collazt(i)
def get_submatrix(matrix, row, col):
    """Trả về ma trận con bằng cách loại bỏ hàng và cột."""
    return [ [matrix[i][j] for j in range(len(matrix)) if j != col] for i in range(len(matrix)) if i != row]

def determinant(matrix):
    """Tính định thức của ma trận."""
    # Nếu là ma trận 1x1, trả về phần tử duy nhất
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Nếu là ma trận 2x2, áp dụng công thức cơ bản
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Khai triển theo hàng đầu tiên
    det = 0
    for col in range(len(matrix)):
        submatrix = get_submatrix(matrix, 0, col)
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(submatrix)
        det += cofactor
    
    return det

# Ví dụ: Ma trận 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 9, 9]
]

det = determinant(matrix)
print(f"Định thức của ma trận là: {det}")
print(get_submatrix(matrix, 3,3))
a=[]
InputMatran(a)
PrintMatran(a)
print(get_submatrix(matrix, 3,3))