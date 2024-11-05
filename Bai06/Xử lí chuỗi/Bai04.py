def ktchuoidx(a):
    dodai = len(a)
    i=0
    while(i<=dodai-1):
        if a[i]==a[dodai-1]:
            i+=1
            dodai-=1
        else:
            return False
    return True
chuoi = str(input("Nhập chuỗi: "))
if ktchuoidx(chuoi):
    print("Đây là chuỗi đối xứng!")
else:
    print("Đây không phải là chuỗi đối xứng!")