import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ans = []

    if n % 2 == 1:
        ans = [3, 1, 2]

        for i in range(4, n, 2):
            ans.append(i + 1)
            ans.append(i)

        print(*ans)
        continue

    for i in range(1, n, 2):
        ans.append(i + 1)
        ans.append(i)

    print(*ans)