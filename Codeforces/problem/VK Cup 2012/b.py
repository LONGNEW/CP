import sys
import math

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cnt = [0] * 5

for item in data:
    cnt[item] += 1

ans = cnt[4]
for i in range