class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
    def Xuat(self):
        print("Tên: ", self.name)
        print("Năm sinh: ", self.yob)
    def Them(self):
        self.name = input("Nhập tên: ")
        while int(self.yob) <= 0:
            self.yob = input("Nhập năm sinh: ")
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    def Xuat(self):
        super().Xuat()
        print("Đang học lớp: ", self.grade)
    def Them(self):
        super().Them()
        self.grade = input("Nhập lớp đang học: ")
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
    def Xuat(self):
        super().Xuat()
        print("Đang dạy môn: ", self.subject)
    def Them(self):
        super().Them()
        self.subject = input("Nhập môn đang dạy: ")
class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    def Xuat(self):
        super().Xuat()
        print("Chuyên ngành bác sĩ: ", self.specialist)
    def Them(self):
        super().Them()
        self.specialist = input("Nhập chuyên ngành bác sĩ: ")
class Ward:
    def __init__(self, name, residents=None):
        self.name = name
        self.residents = residents if residents is not None else []
    def Xuat(self):
        print("Tỉnh: ", self.name)
        print("Cư dân của tỉnh lần lượt là: ")
        for resident in self.residents:
            resident.Xuat()
            print()
    def addPerson(self):
        print("Bạn muốn thêm?")
        print("1. Học sinh", "2. Giáo viên", "3. Bác sĩ", sep="\n")
        choice = int(input())
        person_type = None
        if choice == 1:
            person_type = Student("", 0, "")
        elif choice == 2:
            person_type = Teacher("", 0, "")
        elif choice == 3:
            person_type = Doctor("", 0, "")    
        if person_type:
            person_type.Them()
            self.residents.append(person_type)
a = Student("Sáng", 2005, "Năm 2 đại học")
b = Teacher("Lưu", 2005, "CNTT")
c = Doctor("Tuấn", 2005, "Nha khoa")
Tinh = Ward("Long An", [a, b, c])
Tinh.Xuat()
Tinh.addPerson()
Tinh.Xuat()