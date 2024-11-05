tunhien = []
binhphuong = []
n = int(input())
for i in range(n+1):
    tunhien.append(i)
    if (i**2<n):
        binhphuong.append(i**2)
print("List số tự nhiên từ 0 -> n: ", tunhien)
print("List số bình phương nhỏ hơn n: ", binhphuong)