import sys

for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    diff = abs(a - b)

    if c > diff * 2 or (diff % 2 == 1 and (a + b) % 2 != 1) or (diff % 2 == 0 and (a + b) % 2 != 0) or a > diff * 2 or b > diff * 2:
        print(-1)
        continue

    if c < diff + 1:
        print(c + diff)
    else:
        print(c - diff)
