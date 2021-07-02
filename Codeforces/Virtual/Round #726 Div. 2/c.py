import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    data.sort()
    if len(data) < 3:
        print(f"{data[0]} {data[1]}")
        continue

    diff = data[1] - data[0]
    idx = 1

    for j in range(2, len(data)):
        if diff > data[j] - data[j - 1]:
            idx = j
            diff = data[j] - data[j - 1]

    for j in range(idx, len(data)):
        print(data[j], end=" ")
    for j in range(idx):
        print(data[j], end=" ")
    print()