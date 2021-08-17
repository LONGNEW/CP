import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    temp, ans = [], 0

    for i in range(n):
        temp.append([data[i], i + 1])

    temp.sort()
    for i in range(n):
        for j in range(i + 1, n):
            if temp[i][0] * temp[j][0] > 2 * n:
                break

            if temp[i][0] * temp[j][0] == temp[i][1] + temp[j][1]:
                ans += 1

    print(ans)