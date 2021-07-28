import sys

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    data = [i * 111 for i in range(11)]
    flag = 0

    for item in data:
        temp = x - item
        if temp < 0:
            break

        if temp % 11 == 0:
            flag = 1
            break

    print("YES" if flag else "NO")