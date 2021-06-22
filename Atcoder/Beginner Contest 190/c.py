import sys


def dfs(idx):
    global ans
    # 기저 사례
    if idx == k:

        cnt = 0
        for a, b in dish:
            if visit[a] and visit[b]:
                cnt += 1
        ans = max(ans, cnt)
        return

    visit[person[idx][0]] += 1
    dfs(idx + 1)
    visit[person[idx][0]] -= 1

    visit[person[idx][1]] += 1
    dfs(idx + 1)
    visit[person[idx][1]] -= 1

n, m = map(int, sys.stdin.readline().split())
dish = []
person = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dish.append((a, b))

k = int(sys.stdin.readline())
for i in range(k):
    c, d = map(int, sys.stdin.readline().split())
    person.append((c, d))

ans = 0
for i in range(2):
    visit = [0] * (n + 1)
    visit[person[0][i]] = 1
    dfs(1)

print(ans)
