FEE = 4
COST = 0.25
def main():
    n = float(input("Nhập quảng đường di chuyển (km): "))
    Tien = FEE + COST*(n*1000/140)
    print("Số tiền phải trả là: ", round(Tien,2))
main()