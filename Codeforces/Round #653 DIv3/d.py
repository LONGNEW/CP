import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))


    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for x in a:
        if x % k not in d:
            d[x % k] = 1
        else:
            d[x % k] += 1

    m = 0
    for x in d:
        if x:
            m = max(m, d[x] * k - x)

    if not m:
        print(m)
    else:
        print(m + 1)