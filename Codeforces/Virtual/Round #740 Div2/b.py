import sys, math

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        a, b = b, a

    small, big = math.floor((a + b) / 2), math.ceil((a + b) / 2)

    start, end = b - big, a + big
    left, right = [i for i in range(start, end, 2)], [i for i in range(end, start - 1, -2)]

    ans = list(set(left + right))
    ans.sort()
    print(len(ans))
    print(*ans)