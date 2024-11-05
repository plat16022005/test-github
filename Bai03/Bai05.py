n = int(input())
chan = []
le = []
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
print(chan, le, sep = "\n")