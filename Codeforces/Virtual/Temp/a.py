import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    small, big = data[:n + 1], data[n:]

    for i in range(n):
        print(small[i], big[i], end=" ")
    print()