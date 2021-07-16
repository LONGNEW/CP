import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp)

data.sort(key=lambda x:x[1])

left, right = 0, n - 1
ans, cnt = 0, 0

while left <= right:
    if cnt >= data[left][1]:
        ans += data[left][0]
        cnt += data[left][0]
        left += 1
    else:
        if data[right][0] > data[left][1] - cnt:
            data[right][0] -= data[left][1] - cnt
            ans += (data[left][1] - cnt) * 2
            cnt += data[left][1] - cnt
        else:
            cnt += data[right][0]
            ans += data[right][0] * 2
            right -= 1

print(ans)