import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    if (n + 1) // 2 <= k:
        print(-1)
        continue

    ans = [0] * n
    idx = 1
    for i in range(k):
        ans[idx] = n
        idx += 2
        n -= 1

    for i in range(len(ans)):
        if ans[i] == 0:
            ans[i] = n
            n -= 1

    print(*ans)