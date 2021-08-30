import sys

for i in range(int(sys.stdin.readline())):
    c, d = map(int, sys.stdin.readline().split())

    if abs(c - d) % 2 == 1:
        print(-1)
        continue

    if c + d == 0:
        print(0)
        continue

    if c == d:
        print(1)
        continue

    print(2)
