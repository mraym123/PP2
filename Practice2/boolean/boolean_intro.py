# boolean_intro.py

a = 10
b = 5

# Сравнения
print(a > b)    # True
print(a < b)    # False
print(a == b)   # False
print(a != b)   # True

# Boolean с числами
print(bool(0))      # False
print(bool(1))      # True
print(bool(-3))     # True

# Boolean с условиями
age = 18
is_adult = age >= 18
print(is_adult)     # True

# Boolean в if
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
