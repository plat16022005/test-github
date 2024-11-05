def ky_tu_xuat_hien_nhieu(a):
    dict = {}
    for i in a:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    lon = int()
    kytu = str()
    for i,j in dict.items():
        if j > lon:
            lon = j
            kytu = i
    return kytu, lon
def main():
    a = str(input("Nhập chuỗi: "))
    kytu, lon = ky_tu_xuat_hien_nhieu(a)
    print("Ký tự xuất hiện nhiều lần nhất là: {0}, với số lần xuất hiện là: {1}".format(kytu,lon))
main()