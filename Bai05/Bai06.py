def binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        return None
def hex_to_decimal(hex_str):
    try:
        return int(hex_str, 16)
    except ValueError:
        return None
def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]
def decimal_to_hex(decimal_num):
    return hex(decimal_num)[2:]
def main():
    source_base = input("Nhập hệ thống số hiện tại (2, 10, hoặc 16): ")
    value = input("Nhập giá trị số cần chuyển đổi: ")
    target_base = input("Nhập hệ thống số muốn chuyển đổi sang (2, 10, hoặc 16): ")
    if source_base == "2":
        decimal_value = binary_to_decimal(value)
        if decimal_value is None:
            print("Giá trị nhập không phải là số nhị phân hợp lệ.")
            return
    elif source_base == "10":
        try:
            decimal_value = int(value)
        except ValueError:
            print("Giá trị nhập không phải là số thập phân hợp lệ.")
            return
    elif source_base == "16":
        decimal_value = hex_to_decimal(value)
        if decimal_value is None:
            print("Giá trị nhập không phải là số thập lục phân hợp lệ.")
            return
    else:
        print("Hệ thống số không được hỗ trợ.")
        return
    if target_base == "2":
        print(f"Giá trị trong hệ nhị phân là: {decimal_to_binary(decimal_value)}")

    elif target_base == "10":
        print(f"Giá trị trong hệ thập phân là: {decimal_value}")

    elif target_base == "16":
        print(f"Giá trị trong hệ thập lục phân là: {decimal_to_hex(decimal_value)}")

    else:
        print("Hệ thống số đích không được hỗ trợ.")
main()