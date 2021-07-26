import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    xr = 0
    for item in data:
        xr ^= item

    if xr == 0:
        print("YES")
        continue

    temp, cnt = 0, 0
    for item in data:
        temp ^= item
        if temp == xr:
            temp = 0
            cnt += 1
            continue

    if cnt >= 3:
        print("YES")
    else:
        print("NO")
