import math
number_sides = int(input("Input number of sides: "))
length_sides = int(input("Input the length of a side: "))
area = (number_sides*length_sides**2)/(4*math.tan(math.pi/number_sides))
print("The area of the polygon is:", int(area))