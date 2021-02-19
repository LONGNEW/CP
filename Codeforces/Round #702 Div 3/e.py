import sys

t = int(sys.stdin.readline())
for i in range(t):

    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    temp = []
    for idx, item in enumerate(data):
        temp.append((idx + 1, item))
    temp.sort(key=lambda x:x[1])

    ret = 0
    ans = []
    for idx, item in temp:
        if ret < item:
            ans = []
        ret += item
        ans.append(idx)

    ans.sort()

    print(len(ans))
    for idx in ans:
        print(idx, end=" ")
    print()