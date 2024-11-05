a=[]
n = int(input("Hãy nhập số lượng phần tử của list: "))
for i in range(n):
    x = int(input())
    a.append(x)
a.sort()
print(a)