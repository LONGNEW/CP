import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    monsters = []

    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        need_power, level_up = -float('inf'), temp[0]

        for i in range(1, 1 + level_up):
            need_power = max(need_power, temp[i] - i + 1)

        monsters.append((need_power, level_up))

    monsters.sort()
    level, need_power = 0, -float('inf')
    for i in range(n):
        need_power = max(need_power, monsters[i][0] - level + 1)
        level += monsters[i][1]

    print(need_power)