def kiem_tra_dao_nguoc(a,b):
    if len(a) != len(b):
        return False
    for i,j in zip(reversed(a),b):
        if i != j:
            return False
    return True
def main():
    a = str(input("Nhập chuỗi: "))
    b = str(input("Nhập chuỗi để kiểm tra: "))
    if kiem_tra_dao_nguoc(a,b):
        print("Hai chuỗi chuỗi bạn vừa nhập đảo ngược nhau!")
    else:
        print("Hai chuỗi không đảo ngược nhau")
main()