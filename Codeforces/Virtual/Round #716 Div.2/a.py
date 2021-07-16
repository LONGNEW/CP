import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    flag = 0

    for item in data:
        if math.sqrt(item) != int(math.sqrt(item)):
            flag = 1
            break

    if flag:
        print("YES")
    else:
        print("NO")