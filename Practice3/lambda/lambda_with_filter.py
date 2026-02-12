numbers = [1,2,3,4,5,6,7,8]
even = list(filter(lambda a:a%2==0, numbers))
sq = list(map(lambda a:a**2, even))
print(sq)