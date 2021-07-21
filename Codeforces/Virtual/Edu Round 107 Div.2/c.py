import sys
from collections import deque

n, q = map(int, sys.stdin.readline().split())
color = list(map(int, sys.stdin.readline().split()))
query = list(map(int, sys.stdin.readline().split()))
q = deque(color)

for item in query:
    idx = q.index(item)
    print(idx + 1, end=" ")

    q.remove(item)
    q.appendleft(item)