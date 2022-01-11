import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b, c = list(map(int, sys.stdin.readline().split()))

    d = b - a
    if (2 * b - a) % c == 0 and (2 * b - a) > 0:
        print("YES")
        continue

    d = b - c
    if (2 * b - c) % a == 0 and (2 * b - c) > 0:
        print("YES")
        continue

    total = a + c
    if (total / 2) % b == 0 and total / 2 != b:
        print("YES")
        continue
    print("NO")
