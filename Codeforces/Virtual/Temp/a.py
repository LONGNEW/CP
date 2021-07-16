import sys

k = int(sys.stdin.readline())
for _ in range(k):
    n, x, t = map(int, sys.stdin.readline().split())
    remain = t // x

    if n > remain:
        ans = (n - remain) * remain + remain * (remain - 1) // 2
        print(ans)
    else:
        print(n * (n - 1) // 2)
