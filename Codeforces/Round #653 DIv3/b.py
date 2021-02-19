import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())

    cnt = 0
    while n % 3 == 0:

        if n % 2:
            n *= 2
            cnt += 1

        n /= 6
        cnt += 1

    if n == 1:
        print(cnt)
    else:
        print(-1)
