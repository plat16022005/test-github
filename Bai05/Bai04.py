def KtSoNT(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
def main():
    n = int(input())
    m = n
    while (True):
        m += 1
        if KtSoNT(m):
            break
    print("Số nguyên tố gần nhất và lớn hơn {0} là: ".format(n), m)
main()