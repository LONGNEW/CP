import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(sys.stdin.readline().rstrip())

    for i in range(len(data)):
        if data[i] == 'L' or data[i] == 'R':

            continue

        if data[i] == 'U':
            data[i] = 'D'
        else:
            data[i] = 'U'

    print("".join(data))