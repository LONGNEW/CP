import sys
from math import ceil

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    date = []
    friends = [0] * (n + 1)
    ans = [0] * m
    limit = ceil(m / 2)

    for i in range(m):
        temp = list(map(int, sys.stdin.readline().split()))
        date.append(temp[1:])

        if temp[0] == 1:
            friends[temp[1]] += 1
            ans[i] = temp[1]
            continue

    if max(friends) > limit:
        print("NO")
        continue

    for i in range(m):
        if ans[i] != 0:
            continue

        for j in range(len(date[i])):
            if friends[date[i][j]] < limit:
                friends[date[i][j]] += 1
                ans[i] = date[i][j]
                break

    print("YES")
    print(*ans)