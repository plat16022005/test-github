def TietKiem(a):
    if a < 10:
        return "Tiết kiệm"
    else:
        return "Xài hao quá!"
def main():
    n = int(input())
    print(TietKiem(n))
main()