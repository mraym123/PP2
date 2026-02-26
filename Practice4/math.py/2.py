height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
area = ((base1 + base2) * height)/2
print("Expected Output:",area) 


#with import math
import math

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = math.fsum([base1, base2]) * height / 2

print("Expected Output:", area)
