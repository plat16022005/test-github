students = []
def add_student(student_id, student_name):
    student = {
        "id": student_id,
        "name": student_name
    }
    students.append(student)
    print(f"Đã thêm sinh viên: {student_id} - {student_name}")
def remove_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print(f"Đã xóa sinh viên có mã: {student_id}")
            return
    print("Sinh viên không tồn tại.")
def update_student(student_id, new_name):
    for student in students:
        if student["id"] == student_id:
            student["name"] = new_name
            print(f"Đã sửa sinh viên {student_id} thành {new_name}")
            return
    print("Sinh viên không tồn tại.")
def view_students():
    if not students:
        print("Danh sách sinh viên rỗng.")
        return
    print("Danh sách sinh viên:")
    for student in students:
        print(f"Mã sinh viên: {student['id']}, Tên sinh viên: {student['name']}")
def main():
    while True:
        print("\n--- Quản lý sinh viên ---")
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xem danh sách sinh viên")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':
            student_id = input("Nhập mã sinh viên: ")
            student_name = input("Nhập tên sinh viên: ")
            add_student(student_id, student_name)
        elif choice == '2':
            student_id = input("Nhập mã sinh viên cần xóa: ")
            remove_student(student_id)
        elif choice == '3':
            student_id = input("Nhập mã sinh viên cần sửa: ")
            new_name = input("Nhập tên mới: ")
            update_student(student_id, new_name)
        elif choice == '4':
            view_students()
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
if __name__ == "__main__":
    main()