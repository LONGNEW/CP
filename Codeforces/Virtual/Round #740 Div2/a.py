import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    ans = []

    for i in range(n):
        temp = 0

        for j in range(i % 2, n, 2):
            if j + 1 < n and data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                temp += 1
        ans.append(temp)

    temp = 0
    for i in range(n - 1, -1, -1):
        if ans[i] != 0:
            temp = i + 1
            break

    print(temp)