import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ans = 1

    while ans <= n:
        ans *= 2

    if ans != 1:
        ans //= 2

    print(ans - 1)