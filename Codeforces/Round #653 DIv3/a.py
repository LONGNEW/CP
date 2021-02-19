import sys

t = int(sys.stdin.readline())
for i in range(t):
    x, y, n = map(int, sys.stdin.readline().split())
    limit = n // x
    if x * limit + y > n:
        print(x * limit - (x - y))
    else:
        print(x * limit + y)