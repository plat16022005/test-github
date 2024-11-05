a=[]
dem=int()
tong = int()
n = int(input("Nhập số lượng phần tử của List: "))
for i in range(n):
    x = int(input())
    a.append(x)
    tong += x
tb = float(tong/n)
for i in range(n):
    if (a[i]>tb):
        dem += 1
print("Số lượng phần tử lớn hơn giá trị trung bình là: ", dem)