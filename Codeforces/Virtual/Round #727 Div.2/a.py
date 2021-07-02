import sys

k = int(sys.stdin.readline())
data = []
for i in range(k):
    n, x, t = map(int, sys.stdin.readline().split())
    term = t // x
    remain = n - term

    if remain > 0:
        print(remain * term + (term - 1) * term // 2)
    else:
        print(n * (n - 1) // 2)