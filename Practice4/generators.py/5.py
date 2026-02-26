def countdown(n):
    for i in range(n, -1,-1): #stop at 0(inclusive)
        yield i
N = int(input())
for i in countdown(N):
    print(i)