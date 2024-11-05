import random
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
    mk = ""
    l = []
    while ktmk(mk) == False:
        mk = ""
        l = []
        dodai = random.randint(8,12)
        for i in range(dodai):
            l.append(random.randint(33,122))
        for i in l:
            mk += chr(i)
    print("Mật khẩu tạo ngẫu nhiên: ", mk)
main()