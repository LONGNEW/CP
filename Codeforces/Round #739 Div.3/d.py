import sys

temp = []
i = 1
while i < 10 ** 18:
    temp.append(i)
    i *= 2

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().rstrip()
    ans = float('inf')

    for item in temp:
        item = str(item)
        idx, target_idx = 0, 0

        while idx < len(n) and target_idx < len(item):
            if n[idx] == item[target_idx]:
                target_idx += 1

            idx += 1

        ans = min(ans, len(n) + len(item) - 2 * target_idx)

    print(ans)