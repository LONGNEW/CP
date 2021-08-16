import sys

for _ in range(int(sys.stdin.readline())):
    n, k1, k2 = map(int, sys.stdin.readline().split())
    w, b = map(int, sys.stdin.readline().split())

    white = k1 + k2
    black = 2 * n - white

    print("YES" if white >= w * 2 and black >= b * 2 else "NO")