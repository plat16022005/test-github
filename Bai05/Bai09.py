def SoSaoTietKiem(a):
    if a<2:
        return 5
    elif 2<=a and a<4:
        return 4
    elif 4<=a and a<6:
        return 3
    elif 6<=a and a<10:
        return 2
    elif a>=10:
        return 1
    else:
        pass
def main():
    n = int(input())
    Sao = SoSaoTietKiem(n)
    if Sao >= 3:
        print("Tiết kiệm")
    else:
        print("Xài hao vậy?")
main()