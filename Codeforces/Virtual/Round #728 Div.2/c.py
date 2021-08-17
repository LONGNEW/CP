import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = [0] + list(map(int, sys.stdin.readline().split()))
    temp = [0] * (n + 1)

    data.sort()
    for i in range(1, n + 1):
        temp[i] = temp[i - 1] + data[i]

    ans = data[-1]
    for i in range(1, n + 1):
        ans -= data[i] * (i - 1) - temp[i - 1]

    print(ans)