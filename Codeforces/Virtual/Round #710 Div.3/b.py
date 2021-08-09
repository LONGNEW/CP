import sys

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    data = list(sys.stdin.readline().rstrip())
    stars = []

    for idx, item in enumerate(data):
        if item == '*':
            stars.append(idx)

    if len(stars) == 1:
        print(1)
        continue

    ans, now = 1, stars[0]

    for i in range(1, len(stars)):
        if now + k < stars[i]:
            ans += 1
            now = stars[i - 1]

    print(ans if now == stars[-1] else ans + 1)

