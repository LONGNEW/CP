import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
basic = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
update = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
for x in range(n):
    for y in range(m):
        if visit[x][y] != 0:
            continue

        if basic[x][y] != update[x][y] and cnt == 1:
            cnt += 1
            break

        pivot = basic[x][y]
        if basic[x][y] != update[x][y]:
            cnt += 1
            q = deque([(x, y)])
            basic[x][y] = update[x][y]
            visit[x][y] = 1

            while q:
                now_x, now_y = q.popleft()

                for i in range(4):
                    next_x = dx[i] + now_x
                    next_y = dy[i] + now_y

                    if next_y < 0 or next_x < 0 or next_y >= m or next_x >= n:
                        continue

                    if visit[next_x][next_y] == 0 and basic[next_x][next_y] == pivot:
                        visit[next_x][next_y] = 1
                        basic[next_x][next_y] = update[x][y]
                        q.append((next_x, next_y))

if basic == update and cnt < 2:
    print("YES")
    exit(0)

print("NO")