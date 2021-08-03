import sys

for _ in range(int(sys.stdin.readline())):
    n, w = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    temp = dict()
    data.sort()

    for item in data:
        if item not in temp:
            temp[item] = 1
        else:
            temp[item] += 1

    remain, ans, keys = w, 1, len(data)
    while keys > 0:
        now_add = -float('inf')
        for key in temp.keys():
            if remain < key:
                break
            now_add = key

        if now_add == -float('inf'):
            remain = w
            ans += 1
            continue

        remain -= now_add
        temp[now_add] -= 1

        if temp[now_add] == 0:
            del temp[now_add]

        if remain <= 0:
            ans += 1
            if remain == 0:
                remain = w
            else:
                remain = w - now_add

        keys -= 1

    print(ans - 1 if remain == w else ans)