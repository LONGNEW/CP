import sys

t = int(sys.stdin.readline())
for x in range(t):
    n, m, i, j = map(int, sys.stdin.readline().split())
    print(f"1 1 {n} {m}")