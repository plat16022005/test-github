n = int(input())
a=[]
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(n):
    if a[i] % 2 == 0:
        for j in range(i,n):
            if (a[i]>a[j] and a[j]%2==0):
                a[i],a[j] = a[j],a[i]
    else:
        for j in range(i,n):
            if (a[i]<a[j] and a[j]%2!=0):
                a[i],a[j] = a[j],a[i]
print(a)