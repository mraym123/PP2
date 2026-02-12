class Student:
    school = "High school #12"
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def info(self):
        return f"{self.name} has grade {self.grade} and studies in {Student.school}"
student1 = Student("Jake", 45)
student2 = Student("Alex", 23)
print(student1.info())
print(student2.info())

Student.school = "High school #45" #change the school
print(student1.info())
print(student2.info())