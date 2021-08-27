import sys

for _ in range(int(sys.stdin.readline())):
    l, r = map(int, sys.stdin.readline().split())

    if l == r:
        print(0)
        continue

    start = r // 2
    if start < l:
        print(r % l)
        continue

    print(r % (start + 1))
