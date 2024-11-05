def sont(x):
    if x == 1:
        return False
    for i in range(2,x,1):
        if (x%i==0):
            return False
    return True
n = int(input())
nt=[]
for i in range(n):
    x = int(input())
    if (sont(x)):
        nt.append(x)
print(nt)