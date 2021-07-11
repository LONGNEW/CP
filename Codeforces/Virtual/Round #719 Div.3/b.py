import sys

data = []
for j in range(1, 10):
    num = j
    data.append(num)
    while num < 1000000000:
        num *= 10
        num += j
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