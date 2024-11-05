def get_filename_with_extension(path):
    return path.split('\\')[-1] if '\\' in path else path.split('/')[-1]

def get_filename_without_extension(path):
    filename_with_ext = get_filename_with_extension(path)
    return filename_with_ext.split('.')[0]
def main():
    path = input("Nhập đường dẫn: ")
    filename_with_ext = get_filename_with_extension(path)
    print("Tên file có phần mở rộng: ", filename_with_ext)
    filename_without_ext = get_filename_without_extension(path)
    print("Tên file không có phần mở rộng: ", filename_without_ext)
main()
