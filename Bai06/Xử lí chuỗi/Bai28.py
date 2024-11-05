def is_symmetrical(s):
    n = len(s)
    if n % 2 == 0:
        first_half = s[:n//2]
        second_half = s[n//2:]
    else:
        first_half = s[:n//2]
        second_half = s[n//2+1:]
    return first_half == second_half
def main():
    s = input("Nhập chuỗi: ")
    if is_symmetrical(s):
        print("Chuỗi là symmetrical.")
    else:
        print("Chuỗi không phải là symmetrical.")
main()