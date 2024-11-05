def tim_chuoi_con(a, b):
    s = ""
    l = []
    for i in range(len(a)):
        for j in a[i:]:
            s += j
            if (len(s)>=b):
                l.append(s)
        s = ""
    return l
def main():
    a = input("Nhập chuỗi: ")
    b = int(input("Nhập số: "))
    print("Chuỗi con thõa điều kiện: ", tim_chuoi_con(a,b))
main()