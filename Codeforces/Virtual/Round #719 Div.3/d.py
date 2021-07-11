import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    temp = dict()

    ans = 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] - i - 1 not in temp:
            temp[data[i] - i - 1] = 1
        else:
            temp[data[i] - i - 1] += 1
        ans += temp[data[i] - i - 1] - 1
    print(ans)
