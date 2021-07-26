import sys

for _ in range(int(sys.stdin.readline())):
    n, l, r, s = map(int, sys.stdin.readline().split())
    k = r - l + 1

    low_sum, high_sum = sum(range(1, k + 1)), sum(range(n - k + 1, n + 1))
    if s < low_sum or high_sum < s:
        print(-1)
        continue

    idx, limit = k, n
    temp = [i for i in range(k + 1)]
    while sum(temp) != s:
        temp[idx] += 1

        if temp[idx] == limit:
            idx -= 1
            limit -= 1

    ans, idx, num = [], 1, 1
    for i in range(1, n + 1):
        if l <= i <= r:
            ans.append(temp[idx])
            idx += 1
            continue

        while num in temp:
            num += 1
        ans.append(num)
        num += 1


    print(*ans)