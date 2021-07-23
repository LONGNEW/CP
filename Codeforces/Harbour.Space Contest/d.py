import sys

t = int(sys.stdin.readline())
for _ in range(t):
    data = sys.stdin.readline().rstrip()
    target = sys.stdin.readline().rstrip()
    data_idx, target_idx = len(data) - 1, len(target) - 1

    while data_idx >= 0 and target_idx >= 0:
        if data[data_idx] == target[target_idx]:
            data_idx -= 1
            target_idx -= 1
            continue

        data_idx -= 2

    print("YES" if target_idx == -1 else "NO")