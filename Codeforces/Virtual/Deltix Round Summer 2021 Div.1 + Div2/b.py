import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    pos, idx = [[], []], data[0] % 2

    for i in range(n):
        pos[data[i] % 2].append(i)

    if len(pos[0]) not in [n // 2, n // 2 + 1] or len(pos[1]) not in [n // 2, n // 2 + 1]:
        print(-1)
        continue

    spot1, ans = [i for i in range(0, n, 2)], float('inf')

    for i in range(len(pos)):
        if len(pos[i]) != len(spot1):
            continue

        temp_ans = 0
        for j in range(len(pos[i])):
            temp_ans += abs(spot1[j] - pos[i][j])
        ans = min(temp_ans, ans)

    print(ans)
