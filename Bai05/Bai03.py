def KtSoNT(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
def main():
    a = int(input("Nhập số: "))
    if KtSoNT(a):
        print("Đây là số nguyên tố")
    else:
        print("Đây không phải là số nguyên tố")
main()