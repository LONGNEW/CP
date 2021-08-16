import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (n + 1)
    temp = dict()

    for idx in range(1, n + 1):
        # 현재 인덱스에서의 값이 동일하든 아니든
        # 앞에서 얻은 weight는 계속 남아있게 된다.
        dp[idx] += dp[idx - 1]

        if data[idx - 1] in temp:
            dp[idx] += temp[data[idx - 1]]
        else:
            temp[data[idx - 1]] = 0
        # 동일한 원소의 개수를 다르게 가져가는 부분배열이라고 볼 때
        # 가장 가까운 것이 1개의 원소를 가져간다고 보고
        # 그 다음에는 2개의 원소를 가져가고 라고 생각을 하자.
        # 그렇게 볼 경우 weight를
        temp[data[idx - 1]] += idx

    print(sum(dp))

