import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    data.sort()
    cnt = 1
    prev = data[0]
    diff = float('INF')

    for j in range(1, len(data)):
        temp = data[j]

        if diff > abs(prev - temp):
            diff = abs(prev - temp)

        if diff >= temp:
            cnt += 1
            prev = temp

    print(cnt)

