import sys
from math import gcd, ceil

t = int(sys.stdin.readline())
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    flag = 0
    for a in range(1, ceil(n / 2) + 1):
        for b in range(a, ceil(n / 2) + 1):
            c = n - b - a
            if c < b:
                break

            temp = a * b // gcd(a, b)
            temp = c * temp // gcd(c, temp)
            if temp <= n / 2:
                print(a, b, c)
                flag = 1
                break
        if flag:
            break
