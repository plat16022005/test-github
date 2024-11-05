n = int(input())
a = []
b = []
for i in range(n):
    x = int(input())
    a.append(x)
k = int(input("Nhập số muốn tìm: "))
for i in range(n):
    if (a[i]!=k):
        b.append(a[i])
print(b)