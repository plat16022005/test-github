a=[]
n = int(input("Hãy nhập giá trị n: "))
max = 1e-100
min = 1e100
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(n):
    if (max < a[i]):
        max = a[i]
    if (min > a[i]):
        min = a[i]
print ("Giá trị lớn nhất: ", max, "Giá trị nhỏ nhất: ", min)