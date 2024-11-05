n = int(input())
a=[]
kq=[]
def uoc(x,y):
    return x % y == 0
def boi(x,y):
    return x % y == 0
for i in range(n):
    x = int(input())
    a.append(x)
k = int(input("Hãy nhập k: "))
for i in range(n):
    if (uoc(k,a[i]) or boi(a[i],k)):
        kq.append(a[i])
print(kq)