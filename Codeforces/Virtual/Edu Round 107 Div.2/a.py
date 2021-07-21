import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    for item in data:
        if item == 1 or item == 3:
            cnt += 1
    print(cnt)