import sys
from math import gcd

n = int(sys.stdin.readline())
down = []
up = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    up.append(a)
    down.append(b)

ans_down = down[0]
for i in range(1, n):
    temp = gcd(ans_down, down[i])
    ans_down = ans_down * down[i] // temp

for i in range(n):
    up[i] *= ans_down // down[i]

ans_up = up[0]
for i in range(1, n):
    ans_up = gcd(ans_up, up[i])

temp = gcd(ans_up, ans_down)
print(ans_up // temp, ans_down // temp)
