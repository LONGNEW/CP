import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    ans = n // 10

    if n % 10 == 9:
        ans += 1

    print(ans)


