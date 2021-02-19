import sys

n, x = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
ret = []

for item in sequence:
    if item != x:
        ret.append(item)

for item in ret:
    print(item, end=" ")
