import sys

for _ in range(int(sys.stdin.readline())):
    n, a = map(int, sys.stdin.readline().split())
    ans = [1] * (a - 3)
    num = n - (a - 3)

    temp = []
    if num == 3:
        temp = [1, 1, 1]
    else:
        k = num // 4

        if num % 4 == 0:
            temp = [k, k, 2 * k]
        elif num % 4 == 1:
            temp = [2 * k, 2 * k, 1]
        elif num % 4 == 2:
            temp = [2 * k, 2 * k, 2]
        else:
            temp = [2 * k + 1, 2 * k + 1, 1]

    ans += temp

    print(*ans)