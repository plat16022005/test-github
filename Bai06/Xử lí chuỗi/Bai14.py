def thay_the_ki_tu(a,b,c):
    s=""
    for i in a:
        if i == b:
            s += c
        else:
            s += i
    return s
def main():
    a = input("Nhập chuỗi: ")
    b = input("Nhập kí tự muốn thay đổi: ")
    c = input("Nhập kí tự thay đổi: ")
    print("Chuỗi sau khi thay đổi: ", thay_the_ki_tu(a,b,c))
main()