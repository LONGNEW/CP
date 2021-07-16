import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    Ts = []
    Ms = []
    flag = 0

    for idx, item in enumerate(data):
        if item == 'M':
            Ms.append(idx)
        else:
            Ts.append(idx)

    if data[0] == 'M' or data[-1] == 'M' or len(Ms) * 3 != n:
        print("NO")
        continue

    for i in range(len(Ms)):
        if Ts[i] > Ms[i] or Ms[i] > Ts[i + len(Ms)]:
            flag = 1
            break

    print("NO" if flag else "YES")