import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    temp = []
    for idx in range(1, len(data)):
        if max(data[idx], data[idx - 1]) > 2 * min(data[idx], data[idx - 1]):
            temp.append((data[idx], data[idx - 1]))

    ans = 0

    while temp:
        big, small = temp.pop()
        cnt = -1
        if small > big:
            big, small = small, big

        while big > small:
            cnt += 1
            big /= 2

        ans += cnt

    print(ans)