import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    temp = dict()

    for i in data:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1

    for key in temp.keys():
        if temp[key] == 1:
            print(data.index(key) + 1)
            continue