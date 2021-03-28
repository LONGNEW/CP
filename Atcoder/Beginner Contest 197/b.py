import sys

h, w, x, y = map(int, sys.stdin.readline().split())
graph = []
for i in range(h):
    graph.append(list(sys.stdin.readline().rstrip()))

ans_x = 0
for i in range(w):
    temp = graph[x - 1][i]
    if temp == '.':
        ans_x += 1
    else:
        if i >= y:
            break
        ans_x = 0

ans_y = 0
for i in range(h):
    temp = graph[i][y - 1]
    if temp == '.':
        ans_y += 1
    else:
        if i >= x:
            break
        ans_y = 0

print(ans_x + ans_y - 1)