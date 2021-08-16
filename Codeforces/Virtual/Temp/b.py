import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    ans, diff = [data[0]], float('inf')

    for i in range(1, len(data)):
        diff = min(diff, abs(ans[-1] - data[i]))
        if data[i] > diff:
            break

        ans.append(data[i])

    print(len(ans))