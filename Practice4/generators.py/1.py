def square(n):
    for i in range(1, n+1):
        yield i * i
N = int(input())
for i in square(N):
    print(i)