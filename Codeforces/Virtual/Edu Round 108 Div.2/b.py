import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    min_val, max_val = data[0], data[0]
    diff = 0

    for idx in range(1, len(data)):
        if data[idx] < data[idx - 1]:
            diff = 1

    if diff == 1:
        if data[0] == 1 or data[-1] == n:
            print(1)
        elif data[-1] == 1 and data[0] == n:
            print(3)
        else:
            print(2)
    else:
        print(0)