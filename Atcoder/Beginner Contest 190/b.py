import sys

n, s, d = map(int, sys.stdin.readline().split())
flag = 0

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if x < s and y > d:
        flag = 1

print("Yes" if flag else "No")