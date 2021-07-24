import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    ans = int(n / 3)

    if n % 3 == 2:
        print(ans, ans + 1)
    elif n % 3 == 0:
        print(ans, ans)
    else:
        print(ans + 1, ans)