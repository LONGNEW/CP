import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))

    idx = 0
    while k > 0 and idx < n - 1:
        if data[idx] < k:
            data[n - 1] += data[idx]
            k -= data[idx]
            data[idx] = 0
        else:
            data[idx] -= k
            data[n - 1] += k
            k = 0

        idx += 1

    for item in data:
        print(item, end=" ")
    print()