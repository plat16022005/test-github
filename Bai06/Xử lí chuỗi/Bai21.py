def dao_chuoi(a):
    return "".join(reversed(a))
def main():
    a = str(input("Nhập chuỗi: "))
    b = dao_chuoi(a)
    print("Chuỗi đảo ngược: ", b)
main()