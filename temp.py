import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline().rstrip())
    data = sys.stdin.readline().rstrip()
    l, r = -1, -1

    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            l, r = i + 1, i + 1 + 1
            break

    print(f"{l} {r}" if l != -1 and r != -1 else f"-1 -1")