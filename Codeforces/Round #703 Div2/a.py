import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))

    total = sum(heights)

    if total >= (len(heights) - 1) * len(heights) // 2:
        print("YES")
    else:
        print("NO")