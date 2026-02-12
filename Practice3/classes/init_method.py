class Student:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
    def passed(self, passing_score=12.5):
        return self.grade>=passing_score
    def info(self):
        status = "passed" if self.passed() else "failed"
        return f"Student {self.name}: grade={self.grade}, {status}"
student1 = Student("Alice", 20)
student2 = Student("Armani", 18)
student3 = Student("Ernar", 10)
student = [student1, student2, student3]
for s in student:
    print(s.info())
