def NagativeNumberIntString(str):
    so = ""
    l = []
    for i in range(len(str)):
        if str[i] == "-" and "1" <= str[i+1] <= "9":
            so += str[i] + str[i+1]
            for j in str[(i+2):]:
                if "0" <= j <= "9":
                    so += j
                else:
                    break
        else:
            if so != "":
                l.append(so) 
            so = ""
    return l
def main():
    a = str(input("Nhập chuỗi: "))
    l = NagativeNumberIntString(a)
    for i in l:
        print(i)
main()