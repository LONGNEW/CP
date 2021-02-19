import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))
    flag = 1

    for j in range(k):
        position = 0
        while position < n - 1 and heights[position] >= heights[position + 1]:
            position += 1

        if position == n - 1:
            flag = 0
            break
        heights[position] += 1

    if flag:
        print(position + 1)
    else:
        print(-1)
