def find_repeated_substrings(s):
    substrings = set()
    repeated_substrings = set()
    for length in range(1, len(s)):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring in substrings:
                repeated_substrings.add(substring)
            else:
                substrings.add(substring)
    return list(repeated_substrings)
def main():
    s = input("Nhập chuỗi: ")
    repeated_substrings = find_repeated_substrings(s)
    if repeated_substrings:
        print("Các xâu con lặp lại:")
        for substring in repeated_substrings:
            print(substring)
    else:
        print("Không có xâu con lặp lại nào.")
main()