import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

BIT = [0] * (n + 1)

def sum(x):
    ans = 0
    while x > 0:
        ans += BIT[x]
        x &= (x - 1)
    return ans

def add(x, val):
    x += 1
    while x <= n:
        BIT[x] += val
        x += (x & -x)

ans = 0
for x in reversed(data):
    ans += sum(x)
    add(x, 1)

for x in data:
    print(ans)
    ans += n - 1 - x * 2