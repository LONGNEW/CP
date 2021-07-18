import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

left, ans = 0, 0
temp = dict()
for right in range(len(data)):
    if data[right] not in temp:
        temp[data[right]] = 1

    else:
        temp[data[right]] += 1

    if right - left >= k - 1:

        if len(temp) > ans:
            ans = len(temp)

        temp[data[left]] -= 1
        if temp[data[left]] == 0:
            del temp[data[left]]

        left += 1

print(ans)