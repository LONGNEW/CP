import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    low, high = 1, 2

    while high <= n:
        low = high
        high *= 2

    print(low - 1)
