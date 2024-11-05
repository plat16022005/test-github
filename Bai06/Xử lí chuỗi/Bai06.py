chuoi = str(input("Nhập chuỗi: "))
for i in range(len(chuoi)):
    if "A" <= chuoi[i] and chuoi[i] <= "Z":
        x = chuoi[i].lower()
        chuoi = chuoi.replace(chuoi[i],x)
    elif "a" <= chuoi[i] and chuoi[i] <= "z":
        x = chuoi[i].upper()
        chuoi = chuoi.replace(chuoi[i],x)
    else:
        pass
print(chuoi)