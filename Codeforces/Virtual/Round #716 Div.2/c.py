import sys
import math

n = int(sys.stdin.readline())
ans = []
cnt = 1

for i in range(1, n):
    if math.gcd(i, n) == 1:
        cnt = (cnt * i) % n
        ans.append(i)

if cnt != 1:
    ans.pop()

print(len(ans))
print(*ans)
