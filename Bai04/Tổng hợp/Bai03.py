DICT = {}
#a)
while(True):
    ten = str(input("Nhập hoạt động (Nhập X để dừng): "))
    ten=ten.lower()
    if ten == "x":
        break
    ten=ten[0].upper()+ten[1:]
    TIME = float(input())
    if ten in DICT:
        DICT[ten] += TIME
    else:
        DICT[ten] = TIME
#b)
for i,j in DICT.items():
    print(i,j,"giờ")
#c)
DICT=sorted(DICT.items(),key=lambda x:x[1])
print("Hai hoạt động được làm nhiều nhất là: ",DICT[-2:])
print("Hai hoạt động được làm ít nhất là: ",DICT[:2])