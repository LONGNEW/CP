import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = sys.stdin.readline().rstrip()
    data = dict()
    red, cnt = 0, 0

    for item in n:
        if item not in data:
            data[item] = 1
        else:
            data[item] += 1

    for key in data.keys():
        if data[key] >= 2:
            red += 1
        else:
            cnt += 1

        if cnt == 2:
            red += 1
            cnt = 0

    print(red)
