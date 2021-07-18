import sys


def check(input):
    global ans

    dp = [[float('inf')] * (w + 1) for _ in range(h + 1)]
    for x in range(h):
        for y in range(w):
            a, from_left, from_up = input[x][y], dp[x][y + 1] + c, dp[x + 1][y] + c
            dp[x + 1][y + 1] = min(a, from_left, from_up)

            ans = min(ans, from_left + a, from_up + a)


h, w, c = map(int, sys.stdin.readline().split())
data = []
for _ in range(h):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)
ans = float('inf')

check(data)
check(data[::-1])
print(ans)