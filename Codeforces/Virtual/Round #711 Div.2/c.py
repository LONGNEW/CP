import sys
mod = int(10 ** 9 + 7)

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())

    if k == 1:
        print(1)
        continue

    if n == 1:
        print(2)
        continue

    now = [0] * (n - 1)
    now[0], ans, direction = 1, 0, 1

    for i in range(k):
        temp, total = [0] * (n - 1), 0

        # from left to right
        if direction == 1:
            for j in range(n - 1):
                total += now[j] % mod
                temp[j] = total

            direction = -direction
        else:
            for j in range(n - 2, -1, -1):
                total += now[j] % mod
                temp[j] = total

            direction = -direction

        now = temp
        ans += total

    print((ans + 1) % mod)