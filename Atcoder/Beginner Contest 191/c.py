import sys

h, w = map(int, sys.stdin.readline().split())
graph = []
for i in range(h):
    temp = list(sys.stdin.readline().strip())
    graph.append(temp)

