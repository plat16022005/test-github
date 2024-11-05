class Person():
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
    def describe(self):
        print(f"Name: {self.name} - YoB: {self.yob} - ", end="")
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    def describe(self):
        super().describe()
        print(f"Grade: {self.grade}")
class Docter(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    def describe(self):
        super().describe()
        print(f"Specialist: {self.specialist}")
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
    def describe(self):
        super().describe()
        print(f"Subject: {self.subject}")
class Ward():
    def __init__(self, name: str):
        self.name = name
        self.person = []
    def addPerson(self, person:Person):
        self.person.append(person)
    def describe(self):
        print(f"Name: {self.name}")
        for i in self.person:
            i.describe()
    def countDoctor(self):
        count = int()
        for i in self.person:
            if isinstance(i, Docter):
                count+=1
        return count
    def sortAge(self):
        self.person = sorted(self.person, key=lambda x:x.yob, reverse=True)
ward1 = Ward("Ward11")
student1 = Student("Tuấn",2005,"Đại học")
teacher1 = Teacher("Lưu", 2004, "Toán")
teacher2 = Teacher("Sáng", 2006, "CNTT")
doctor1 = Docter("Vinh", 2001, "Thú y")
doctor2 = Docter("Thuận", 2003, "Răng hàm mặt")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)
ward1.describe()
print(ward1.countDoctor())
ward1.sortAge()
ward1.describe()