chuoi = str(input("Nhập chuỗi: "))
so = ['1','2','3','4','5','6','7','8','9','0']
dict = {'Số ký tự chữ: ': 0, 'Số kí tự số: ': 0}
for i in chuoi:
    if i in so:
        dict['Số kí tự số: '] += 1
    else:
        dict['Số ký tự chữ: '] += 1
print(dict)