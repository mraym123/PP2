import math
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = math.prod([base, height]) #product of iterables
print("Expected Output:", area)