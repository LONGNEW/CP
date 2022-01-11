import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    data = list(sys.stdin.readline().rstrip())
    ans = [0] * k

    alpha = dict()
    temp = "abcdefghijklmnopqrstuvwxyz"
    for item in temp:
        alpha[item] = 0

    cnt, ones = 0, 0
    for item in data:
        alpha[item] += 1

        if alpha[item] == 2:
            alpha[item] = 0
            cnt += 1

    for key in alpha.keys():
        if alpha[key] == 0:
            continue
        ones += 1

    idx = 0
    while cnt >= k:
        for i in range(k):
            ans[idx] += 2

            idx += 1
            if idx >= k:
                idx = 0
            cnt -= 1

    ones += cnt * 2
    while ans[-1] % 2 == 0 and ones > 0:
        if ans[idx] % 2 != 0:
            continue

        ans[idx] += 1

        idx += 1
        if idx >= k:
            idx = 0
        ones -= 1

    print(min(ans))