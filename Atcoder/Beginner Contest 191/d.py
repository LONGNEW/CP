import sys

x, y, r = map(float, sys.stdin.readline().split())
cnt = 0
xs = []
ys = []
for i in range(int(x - r), int(x + r) + 1):
    xs.append(i)
for i in range(int(y - r), int(y + r) + 1):
    ys.append(i)

for i in xs:
    for j in ys:
        A = (i - x) ** 2
        B = (j - y) ** 2
        if A + B <= r ** 2:
            cnt += 1
print(cnt)