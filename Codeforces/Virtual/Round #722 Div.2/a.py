import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()

    cnt = 0
    prev = data[0]

    for item in data:
        if prev != item:
            break
        cnt += 1

    print(len(data) - cnt)

