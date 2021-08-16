import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    pivot, cnt = data[0], 0

    for item in data:
        if pivot != item:
            break
        cnt += 1

    print(len(data) - cnt)