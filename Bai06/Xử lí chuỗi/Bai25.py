def ktso(a):
    for i in a:
        if "0" <= i <= "9":
            return True
    return False
def ktchu(a):
    for i in a:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            return True
    return False
def ktkitu(a):
    for i in a:
        if not(("a" <= i <= "z" or "A" <= i <= "Z") or ("0" <= i <= "9")):
            return True
    return False
def ktmk(a):
    if len(a) < 8:
        return False
    if ktso(a) and ktchu(a) and ktkitu(a):
        return True
    else:
        return False
def main():
    a = str(input("Nhập mật khẩu: "))
    if ktmk(a):
        print("Mật khẩu mạnh")
    else:
        print("mật khẩu yếu")
main()