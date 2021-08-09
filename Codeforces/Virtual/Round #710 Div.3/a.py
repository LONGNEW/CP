import sys

for _ in range(int(sys.stdin.readline())):
    n, m, x = map(int, sys.stdin.readline().split())
    col = (x - 1) // n
    row = (x - 1) % n
    ans = 1 + row * m + col

    print(ans)