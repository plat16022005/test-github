import math
def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            return [] if c != 0 else ["Vô số nghiệm"]
        return [-c / b]
    delta = b**2 - 4*a*c
    if delta < 0:
        return []
    elif delta == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return [x1, x2]
def main():
    a = int(input("Nhập hệ số a theo ax2 + bx + c = 0: "))
    b = int(input("Nhập hệ số b theo ax2 + bx + c = 0: "))
    c = int(input("Nhập hệ số c theo ax2 + bx + c = 0: "))
    print("Nghiệm của phương trình bậc hai {0}x2 + {1}x + {2} = 0 là: ".format(a,b,c), giai_phuong_trinh_bac_hai(a,b,c))
main()