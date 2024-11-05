n = int(input())
a=[]
am = []
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(n):
    if a[i] < 0:
        for j in range(i,n):
            if (a[i]<a[j]):
                a[i],a[j] = a[j],a[i]
print(a)