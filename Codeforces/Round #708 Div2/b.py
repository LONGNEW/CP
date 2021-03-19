import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))

    num = [0] * m
    for item in data:
        num[item % m] += 1

    ans = 0
    if num[0] != 0:
        ans += 1
        num[0] = 0

    for start in range(1, m // 2 + 1):

        end = m - start

        temp = min(num[start], num[end])
        if temp != 0:
            ans += 1

            if start == end:
                num[start] = 0
                continue

            if num[start] == num[end]:
                num[end] -= temp
                num[start] -= temp
                continue

            if num[start] == temp:
                num[end] -= temp + 1
                num[start] -= temp
            else:
                num[start] -= temp + 1
                num[end] -= temp
    ans += sum(num)
    print(ans)