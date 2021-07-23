import sys
sys.setrecursionlimit(100000)

def check(idx, target_idx, direction):
    if target_idx == len(target) - 1:
        return True

    if idx - 1 >= 0 and data[idx - 1] == target[target_idx + 1]:
        if check(idx - 1, target_idx + 1, 0):
            return True

    if direction == 1 and idx + 1 < len(data) and data[idx + 1] == target[target_idx + 1]:
        if check(idx + 1, target_idx + 1, 1):
            return True

    return False

t = int(sys.stdin.readline())
for _ in range(t):
    data = sys.stdin.readline().rstrip()
    target = sys.stdin.readline().rstrip()
    start = []

    for i in range(len(data)):
        if target[0] == data[i]:
            start.append(i)

    flag = False
    for idx in start:
        flag = check(idx, 0, 1)
        if flag:
            break

    print("YES" if flag else "NO")
