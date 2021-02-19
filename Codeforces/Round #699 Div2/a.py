import sys
from collections import Counter

t = int(sys.stdin.readline())
for i in range(t):
    target_x, target_y = map(int, sys.stdin.readline().split())
    order = list(sys.stdin.readline().strip())
    count = Counter(order)

    ans = 1

    if target_x > 0:
        if count['R'] < target_x:
            ans = 0
    else:
        if count['L'] < abs(target_x):
            ans = 0

    if target_y > 0:
        if count['U'] < target_y:
            ans = 0
    else:
        if count['D'] < abs(target_y):
            ans = 0

    if ans:
        print("YES")
    else:
        print("NO")