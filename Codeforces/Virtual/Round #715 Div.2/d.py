import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data1 = sys.stdin.readline().rstrip()
    data2 = sys.stdin.readline().rstrip()
    data3 = sys.stdin.readline().rstrip()
    p1, p2, p3 = 0, 0, 0
    ans = []

    while p1 < 2 * n and p2 < 2 * n and p3 < 2 * n:
        if data1[p1] == data2[p2]:
            ans.append(data1[p1])
            p1 += 1
            p2 += 1
        elif data1[p1] == data3[p3]:
            ans.append(data1[p1])
            p1 += 1
            p3 += 1
        else:
            ans.append(data2[p2])
            p2 += 1
            p3 += 1

    if p1 == 2 * n:
        if p2 > p3:
            ans.append(data2[p2:])
        else:
            ans.append(data3[p3:])
    elif p2 == 2 * n:
        if p1 > p3:
            ans.append(data1[p1:])
        else:
            ans.append(data3[p3:])
    else:
        if p1 > p2:
            ans.append(data1[p1:])
        else:
            ans.append(data2[p2:])

    print("".join(ans))