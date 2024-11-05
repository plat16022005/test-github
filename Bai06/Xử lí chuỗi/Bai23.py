def kt_email(email):
    if email.count('@') != 1:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    a = parts[0]
    if len(a) == 0:
        return False
    domain_parts = parts[1].split('.')
    if len(domain_parts) != 2:
        return False
    b, c = domain_parts
    if len(b) == 0 or len(c) == 0:
        return False   
    return True
def main():
    email = input("Nhập địa chỉ email: ")
    if kt_email(email):
        print("Địa chỉ email hợp lệ.")
    else:
        print("Địa chỉ email không hợp lệ.") 
main()