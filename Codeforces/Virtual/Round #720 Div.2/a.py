import sys

t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())

    if b == 1:
        print("NO")
        continue

    print("YES")
    print(f"{a} {a * b} {a + a * b}")