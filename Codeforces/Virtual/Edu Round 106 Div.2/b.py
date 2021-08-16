import sys

for _ in range(int(sys.stdin.readline())):
    data = sys.stdin.readline().rstrip()
    zero_idx, one_idx = -1, 101

    for j in range(1, len(data)):
        if data[j] == '0' and data[j] == data[j - 1]:
            zero_idx = max(zero_idx, j)
        elif data[j] == '1' and data[j] == data[j - 1]:
            one_idx = min(one_idx, j)

    print("NO" if zero_idx > one_idx else "YES")