import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    temp_a, temp_b = map(int, sys.stdin.readline().split())
    a, b = temp_a, temp_b
    data = list(sys.stdin.readline().rstrip())
    right_idx, flag = len(data) - 1, 0

    for i in range(math.ceil(len(data) / 2)):
        if data[i] != '?' and data[right_idx] != '?':
            if data[i] != data[right_idx]:
                flag = 1
                break
        right_idx -= 1

    if (a % 2 == 1 and b % 2 == 1) or flag == 1:
        print(-1)
        continue

    right_idx = len(data) - 1
    for i in range(math.ceil(len(data) / 2)):
        if i == right_idx:
            if data[i] == '0':
                a -= 1
            elif data[i] == '1':
                b -= 1
            continue

        if data[i] != '?' and data[right_idx] == '?':
            if data[i] == '0':
                a -= 2
                data[right_idx] = '0'
            else:
                b -= 2
                data[right_idx] = '1'
        elif data[i] == '?' and data[right_idx] != '?':
            if data[right_idx] == '0':
                a -= 2
                data[i] = '0'
            else:
                b -= 2
                data[i] = '1'
        elif data[i] != '?' and data[right_idx] != '?':
            if data[i] == '0':
                a -= 2
            else:
                b -= 2

        right_idx -= 1
    right_idx = len(data) - 1
    for i in range(math.ceil(len(data) / 2)):
        if i == right_idx:
            if a > 0:
                data[i] = '0'
                a -= 1
            elif b > 0:
                data[i] = '1'
                b -= 1
            continue

        if data[i] == '?':
            if a > 1:
                data[i], data[right_idx] = '0', '0'
                a -= 2
            else:
                data[i], data[right_idx] = '1', '1'
                b -= 2

        right_idx -= 1

    if a == 0 and b == 0:
        for i in data:
            print(i, end="")
        print()
    else:
        print(-1)