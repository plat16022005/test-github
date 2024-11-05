def optimize_string(s):
    s = s.strip()
    words = s.split()
    optimized_string = " ".join(words)
    return optimized_string
def main():
    s = input("Nhập chuỗi: ")
    optimized = optimize_string(s).lower().title()
    print("Chuỗi danh từ tối ưu: ", optimized)
main()