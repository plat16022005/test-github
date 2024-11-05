def string_to_ascii(s):
    ascii_values = [ord(char) for char in s]
    return ascii_values
def ascii_to_string(ascii_list):
    chars = [chr(num) for num in ascii_list]
    return ''.join(chars)
def main():
    choice = input("Chọn hành động (1: Chuỗi sang ASCII, 2: ASCII sang chuỗi): ")
    if choice == '1':
        s = input("Nhập chuỗi: ")
        ascii_values = string_to_ascii(s)
        print("Mã ASCII tương ứng:", ascii_values)
    elif choice == '2':
        ascii_input = input("Nhập danh sách mã ASCII, cách nhau bởi dấu cách: ")
        ascii_list = list(map(int, ascii_input.split()))
        original_string = ascii_to_string(ascii_list)
        print("Chuỗi tương ứng:", original_string)
    else:
        print("Lựa chọn không hợp lệ!")
main()