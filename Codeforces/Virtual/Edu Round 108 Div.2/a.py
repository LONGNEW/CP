import sys

t = int(sys.stdin.readline())
for _ in range(t):
    r, b, d = map(int, sys.stdin.readline().split())

    small = min(r, b)
    big = max(r, b)

    if d == 0:
        print("YES" if r == b else "NO")
    else:
        print("YES" if small * (d + 1) >= big else "NO")