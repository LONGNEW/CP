import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    initial_color = list(map(int, sys.stdin.readline().split()))
    desired_color = list(map(int, sys.stdin.readline().split()))
    color_have = list(map(int, sys.stdin.readline().split()))

