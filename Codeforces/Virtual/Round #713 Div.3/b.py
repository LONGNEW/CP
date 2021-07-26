import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data, pos = [], []
    fir_x, fir_y = 0, 0
    sec_x, sec_y = 0, 0

    for i in range(n):
        temp = list(sys.stdin.readline().rstrip())
        for j in range(n):
            if temp[j] == '*':
                pos.append((i, j))
        data.append(temp)

    # row is equal
    if pos[0][0] == pos[1][0]:
        if pos[0][0] - 1 < 0:
            fir_x, fir_y = pos[0][0] + 1, pos[0][1]
            sec_x, sec_y = pos[1][0] + 1, pos[1][1]
        else:
            fir_x, fir_y = pos[0][0] - 1, pos[0][1]
            sec_x, sec_y = pos[1][0] - 1, pos[1][1]
    elif pos[0][1] == pos[1][1]:
        if pos[0][1] - 1 < 0:
            fir_x, fir_y = pos[0][0], pos[0][1] + 1
            sec_x, sec_y = pos[1][0], pos[1][1] + 1
        else:
            fir_x, fir_y = pos[0][0], pos[0][1] - 1
            sec_x, sec_y = pos[1][0], pos[1][1] - 1
    else:
        fir_x, fir_y = pos[0][0], pos[1][1]
        sec_x, sec_y = pos[1][0], pos[0][1]

    data[fir_x][fir_y] = '*'
    data[sec_x][sec_y] = '*'

    for i in range(n):
        for j in range(n):
            print(data[i][j], end="")
        print()