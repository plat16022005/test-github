def KTvietHoa(a):
    for i in a:
        if "A" <= i and i <= "Z":
            return True
    return False
def KTso(a):
    for i in a:
        if "0" <= i and i <= "9":
            return True
    return False
def KTvietthuong(a):
    for i in a:
        if "a" <= i and i <= "z":
            return True
    return False
def KTmatkhau(chuoi):
    if KTvietHoa(chuoi) and KTso(chuoi) and KTvietthuong(chuoi):
        return True
    else:
        return False
def main():
    chuoi = str(input("Nhập mật khẩu: "))
    if KTmatkhau(chuoi):
        print("Mật khẩu mạnh")
    else:
        print("Mật khẩu yếu xìu")
main()