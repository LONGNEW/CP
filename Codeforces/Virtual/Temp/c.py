import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()

    if len(data) == 2:
        print(*data)
        continue

    idx = -1
    diff = 999999999
    for i in range(1, len(data)):
        if data[i] - data[i - 1] < diff:
            idx = i
            diff = data[i] - data[i - 1]

    print(*data[idx:], *data[:idx])
