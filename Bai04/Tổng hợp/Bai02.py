SET = set()
DICT = {}
chuoi = str(input("Nhập chuỗi: "))
for i in chuoi:
    if i not in SET and (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122):
        SET.add(i)
for i in SET:
    DICT[i] = 0
for i in chuoi:
    if i in SET:
        DICT[i]+=1
print(DICT)