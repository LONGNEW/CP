import sys

v, t, s, d = map(int, sys.stdin.readline().split())

if t * v <= d <= v * s:
    print("No")
else:
    print("Yes")