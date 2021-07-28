import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [[-float('inf')] * (n + 1) for i in range(n + 1)]
# 만들고 있는 dp의 형태가 [pos][drinks]를 기록하기 때문에
# 1행부터 시작을 하지만 점화식의 형태를 그 이전 행에 drinks - 1의 위치에 저장된 값에다가 현재의 음료 값을 더해서 얻기 때문에
# 우선적으로 0을 저장해 둬야 한다.
for i in range(n + 1):
    dp[i][0] = 0

for pos in range(1, n + 1):
    # 마실수 있는 음료의 수는 pos + 1까지 마실 수 있다.
    # pos의 경우 0에서 부터 시작하기 때문에 +1을 해줘야 한다.
    for drink in range(1, pos + 1):
        if dp[pos - 1][drink - 1] + data[pos - 1] >= 0:
            dp[pos][drink] = max(dp[pos - 1][drink - 1] + data[pos - 1], dp[pos - 1][drink])
        else:
            dp[pos][drink] = dp[pos - 1][drink]

ans = 0
for i in range(n + 1):
    if dp[n][i] >= 0:
        ans = i
print(ans)
