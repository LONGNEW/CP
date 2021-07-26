import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()

    x = sum(data) - data[-1] * 2
    if x in data[:len(data) - 1]:
        data.remove(x)
        print(*data[:n])
    else:
        if sum(data[:n]) == data[n]:
            print(*data[:n])
        else:
            print(-1)