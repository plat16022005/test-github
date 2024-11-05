a = []
n = int(input("Nhập số lượng phần tử list: "))
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(n):
    if(a[i]<0):
        print("Vị trí phần tử âm đầu tiên: ", i)
        exit()
print("Không có phần tử âm trong list")