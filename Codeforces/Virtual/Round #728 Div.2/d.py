import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)

data.sort(key=lambda x: x[1])
cnt, ans = 0, 0
left, right = 0, len(data) - 1

while left <= right:
    if data[left][1] <= cnt:
        ans += data[left][0]
        cnt += data[left][0]

        # left에서도 아래에서의 right -= 1에 걸릴 수 있기 때문에 작성이 필요.
        data[left][0] = 0
        left += 1
    else:
        # 아직 bi 기준을 못 채웠기 때문에 음수가 발생할 가능성 없음
        buy = min(data[right][0], data[left][1] - cnt)
        data[right][0] -= buy
        cnt += buy
        ans += buy * 2

        if data[right][0] == 0:
            right -= 1
print(ans)