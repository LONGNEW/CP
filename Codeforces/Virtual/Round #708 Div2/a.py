import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    num, ans, temp = [0] * 101, [], []
    data.sort()

    for item in data:
        if num[item] == 0:
            ans.append(item)
            num[item] += 1
        else:
            temp.append(item)

    ans += temp
    for item in ans:
        print(item, end=" ")
    print()