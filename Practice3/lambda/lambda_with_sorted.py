students_grades = [23, 22, 12, 10, 19, 18, 21]#from total 25
passed = list(filter(lambda x:x>12.5, students_grades))
sorting = sorted(passed, key=lambda x:x)
print(sorting)