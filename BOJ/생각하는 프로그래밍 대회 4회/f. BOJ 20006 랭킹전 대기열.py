import sys

p, m = map(int, sys.stdin.readline().split())
room = [[] for i in range(p)]

for i in range(p):
    l, n = sys.stdin.readline().split()
    for idx, item in enumerate(room):

        if 0 < len(room[idx]) < m:
            pivot_level = item[0][0]

            if pivot_level - 10 <= int(l) <= pivot_level + 10:
                room[idx].append((int(l), n))
                break
        if len(room[idx]) == 0:
            room[idx].append((int(l), n))
            break

for data in room:
    data.sort(key=lambda x: x[1])
    if len(data) == 0:
        continue

    if len(data) == m:
        print("Started!")
        for item in data:
            print(item[0], item[1])
    else:
        print("Waiting!")
        for item in data:
            print(item[0], item[1])
