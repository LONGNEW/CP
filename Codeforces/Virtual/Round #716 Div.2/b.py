import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    ans = 1
    for i in range(k):
        ans = (ans * n) % int(math.pow(10, 9) + 7)
    print(ans)