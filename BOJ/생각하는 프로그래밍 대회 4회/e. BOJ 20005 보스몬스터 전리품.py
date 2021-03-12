import sys
from collections import deque, defaultdict

h, w, p = map(int, sys.stdin.readline().split())
graph = []
player_pos = []
for i in range(h):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)
    for idx, item in enumerate(temp):
        if 97 <= ord(item) <= 122:
            player_pos.append((item, i, idx))

player = defaultdict()
howmany = defaultdict()

for i in range(p):
    account, dps = sys.stdin.readline().split()
    player[account] = int(dps)

boss_hp = int(sys.stdin.readline())
# move = []

for who, x, y in player_pos:
    q = deque([(x, y, 0)])
    visit = [[0] * w for i in range(h)]
    visit[x][y] = 1
    flag = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        now_x, now_y, cnt = q.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == "." and visit[nx][ny] == 0:
                q.append((nx, ny, cnt + 1))
            if graph[nx][ny] == "B":
                player[cnt + 1] += player[who]
                howmany[cnt + 1] += 1
                flag = 1
                break

        if flag:
            break

# move.sort()
now_time, temp_dps, ans = 0, 0, 0
for arrive in range(1, 1000001):
    if arrive == 0:
        continue

    boss_hp -= (arrive - now_time) * temp_dps
    if boss_hp <= 0:
        print(ans)
        break

    boss_hp -= player[arrive]
    if boss_hp <= 0:
        print(ans)
        break

    ans += howmany[arrive]
    now_time = arrive
    temp_dps += player[arrive]

print(ans)
