import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    zero, one, two = 0, 0, 0
    for item in a:
        if item % 3 == 0:
            zero += 1
        elif item % 3 == 1:
            one += 1
        else:
            two += 1

    ans = 0
    ret = n // 3
    while zero != one or zero != two or one != two:
        if two > ret:
            gap = two - ret
            ans += gap
            two -= gap
            zero += gap

        if zero > ret:
            gap = zero - ret
            ans += gap
            zero -= gap
            one += gap

        if one > ret:
            gap = one - ret
            ans += gap
            one -= gap
            two += gap

    print(ans)