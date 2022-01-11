import sys

data = []
for j in range(1, 10):
    num = j
    data.append(num)
    for i in range(1, 10):
        num = num * 10 + j
        data.append(num)
data.sort()

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    cnt = 0

    for item in data:
        if n < item:
            print(cnt)
            break

        cnt += 1