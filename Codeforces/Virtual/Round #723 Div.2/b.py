# solution from meteorexx
import sys

t = int(sys.stdin.readline())
for i in range(t):
    x = int(sys.stdin.readline())
    data = [111 * j for j in range(11)]
    flag = 0

    for item in data:
        if item > x:
            break

        if x - item % 11 == 0:
            flag = 1
            print("YES")
            break

    if flag:
        continue

    print("NO")