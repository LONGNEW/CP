import sys

n, k = map(int, sys.stdin.readline().split())
data = sys.stdin.readline().rstrip()
left, right = 0, 0

for i in range(1, len(data)):
    if data[left] > data[i]:
        # if left is not 0 we need to reset this to 0
        left = 0
        right = i
    elif data[left] == data[i]:
        left += 1
    else:
        break

ans = data[:right + 1]
while len(ans) < k:
    ans += ans
print(ans[:k])