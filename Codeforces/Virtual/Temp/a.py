import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    total = sum(data)

    if total == n:
        print(0)
    elif total < n:
        print(1)
    else:
        print(total - n)