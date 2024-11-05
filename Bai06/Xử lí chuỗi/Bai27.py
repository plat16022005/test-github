# Hàm title() trong Python được sử dụng để chuyển đổi chuỗi thành "title case", tức là mỗi từ trong chuỗi sẽ có chữ cái đầu tiên được viết hoa và các chữ cái khác trong từ đó viết thường. Nó sẽ coi bất kỳ ký tự không phải chữ cái nào (như dấu cách, dấu chấm, v.v.) là dấu phân cách giữa các từ.
s = "xIN cHào! eM LÀ PhẠm lÊ anh TUẤN"
result = s.title()
print(result)
# Hàm translate() được sử dụng để thay thế các ký tự trong chuỗi dựa trên bảng dịch (translation table). Để tạo bảng dịch, bạn có thể sử dụng hàm str.maketrans(). Nó cho phép bạn thay thế hoặc loại bỏ các ký tự cụ thể trong chuỗi.
translation_dict = {ord('a'): '4', ord('e'): '3', ord('i'): '1'}
s = "xiN cHào! eM LÀ PhẠm lÊ anh TUẤN"
translated_string = s.translate(translation_dict)
print(translated_string)