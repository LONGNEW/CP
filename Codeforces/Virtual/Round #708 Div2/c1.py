import sys

for i in range(int(sys.stdin.readline())):
    n, a = map(int, sys.stdin.readline().split())
    ans = []

    if n == 3:
        ans = [1, 1, 1]
    else:
        k = n // 4

        if n % 4 == 0:
            ans = [k, k, 2 * k]
        elif n % 4 == 1:
            ans = [2 * k, 2 * k, 1]
        elif n % 4 == 2:
            ans = [2 * k, 2 * k, 2]
        else:
            ans = [2 * k + 1, 2 * k + 1, 1]

    print(*ans)
