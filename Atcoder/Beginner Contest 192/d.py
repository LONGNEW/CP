import sys
import math

x = list(map(int, sys.stdin.readline().strip()))
m = int(sys.stdin.readline())

idx = max(x) + 1
cnt = 0

while True:
    ret = 0
    for i, item in enumerate(x):
        ret += item * math.pow(idx, (len(x) - 1 - i))

    if ret > m:
        break
    cnt += 1
    idx += 1

print(cnt)