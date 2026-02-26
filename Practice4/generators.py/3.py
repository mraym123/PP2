def divisible_by3_by4(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield i
N = int(input())
for i in divisible_by3_by4(N):
    print(i)