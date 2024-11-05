def tim_chuoi_con(a):
    s = ""
    l = []
    for i in range(len(a)):
        for j in a[i:]:
            s += j
            if (s not in l):
                l.append(s)
        s = ""
    return l
def main():
    a = input("Nhập chuỗi: ")
    print("Chuỗi con thõa điều kiện: ", tim_chuoi_con(a))
main()