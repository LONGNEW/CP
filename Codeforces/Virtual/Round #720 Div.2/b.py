import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    val = min(data)
    idx = data.index(val)
    print(len(data) - 1)
    for j in range(len(data)):
        if j == idx:
            continue
        print(f"{idx + 1} {j + 1} {val} {val + abs(idx - j)}")