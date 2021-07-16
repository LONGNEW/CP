import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    num = [[], []]

    for item in data:
        num[item % 2].append(item)

    print(*num[0], *num[1])
