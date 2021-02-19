import sys

data = [i ** 3 for i in range(1, 10001)]
data_dic = dict()
for item in data:
    data_dic[item] = 1

t = int(sys.stdin.readline())
for i in range(t):
    x = int(sys.stdin.readline())
    flag = 1
    possible = 0

    for item in data:
        if item > x:
            flag = 0
            break
        if data_dic.get(x - item):
            possible = 1
            break

    if not flag:
        print("NO")
    else:
        if not possible:
            print("NO")
        else:
            print("YES")