import sys


def check(arr):
    arr.sort(key=lambda x:x[1])

    stack = []
    for idx, pos, way in arr:
        if way == 'L':
            if not stack:
                # anyway if we still have 'L' then it will work as 'R'
                # so swap it.
                stack.append((idx, -pos))
            else:
                temp = stack.pop()
                ans[idx] = ans[temp[0]] = (pos - temp[1]) // 2
        else:
            stack.append((idx, pos))

    while len(stack) > 1:
        fir = stack.pop()
        sec = stack.pop()

        ans[fir[0]] = ans[sec[0]] = (m + m - fir[1] - sec[1]) // 2


t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    start = list(map(int, sys.stdin.readline().split()))
    direction = list(sys.stdin.readline().split())

    data = [[], []]
    ans = [-1] * (len(start))

    for j in range(len(start)):
        data[start[j] % 2].append((j, start[j], direction[j]))

    check(data[0])
    check(data[1])

    print(*ans)
