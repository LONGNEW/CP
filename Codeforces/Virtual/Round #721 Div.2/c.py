import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (n + 1)
    temp = dict()

    for idx in range(1, n + 1):
        dp[idx] += dp[idx - 1]

        if data[idx - 1] in temp:
            dp[idx] += temp[data[idx - 1]]
        else:
            temp[data[idx - 1]] = 0
        temp[data[idx - 1]] += idx

    print(sum(dp))

