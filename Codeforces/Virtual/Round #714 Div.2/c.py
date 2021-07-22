import sys

dp = [[1] for i in range(10)]
for operation in range(1, 2 * 10 ** 5 + 1):
    for digit in range(10):
        if digit < 9:
            dp[digit].append(dp[digit + 1][operation - 1])
        else:
            dp[digit].append((dp[0][operation - 1] + dp[1][operation - 1]) % (10 ** 9 + 7))

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    ans = 0
    while n:
        ans += dp[n % 10][k]
        n //= 10
        ans %= (10 ** 9 + 7)

    print(ans)
