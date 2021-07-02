import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    compare = sum(data)
    if compare > n:
        print(compare - n)
    elif compare == n:
        print(0)
    else:
        print(1)