import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1 and b == 1 and c == 1:
        print(f"1 1")
        continue

    x = int(math.pow(10, a - 1))
    y = int(math.pow(10, b - 1))
    z = int(math.pow(10, c - 1))

    if x > z:
        print(f"{x + z} {y}")
    else:
        print(f"{x} {y + z}")