import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    temp = [data[0]]
    visit = [0] * 26
    flag = 0

    now = data[0]
    for item in data:
        if now != item:
            now = item
            temp.append(now)

    for item in temp:
        visit[ord(item) - 65] += 1

    for item in visit:
        if item > 1:
            print("NO")
            flag = 1
            break

    if not flag:
        print("YES")
