a = []
n = int(input("Nhập số n: "))
for i in range(n):
    x = int(input())
    if x < 0:
        a.append(x)
if len(a) == 0:
    print ("Mảng bạn nhập không có số âm!")
    exit()
else:
    k=int(input("Nhập số thứ tự k: "))
    if k <= len(a):
        print(a[k-1])
    else:
        print("Không có con số âm thứ k nào mà bạn vừa nhập cả!")
        exit()