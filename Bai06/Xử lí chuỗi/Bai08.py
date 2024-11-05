def sapxep(a):
    return ''.join(sorted(a,reverse=True))
def main():
    a = str(input("Nhập chuỗi: "))
    print("Chuỗi sau khi sắp xếp các kí tự tăng dần là: ", sapxep(a))
main()