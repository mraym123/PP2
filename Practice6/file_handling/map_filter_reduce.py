from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7]


odd = list(filter(lambda x: x % 2 != 0, numbers))


cubed = list(map(lambda x: x**3, odd))


filtered = list(filter(lambda x: x > 50, cubed))


result = reduce(lambda a, b: a * b, filtered)

print(result)