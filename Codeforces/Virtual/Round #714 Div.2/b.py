import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    val = min(data)
    cnt, flag = 0, 0

    for item in data:
        if val == item:
            cnt += 1
            continue

        if val & item != val:
            flag = 1
            break

    if flag:
        print(0)
        continue

    ans = cnt * (cnt - 1)
    for i in range(1, n - 1):
        ans = (ans * i) % int(math.pow(10, 9) + 7)

    print(ans)