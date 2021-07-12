import sys
import math

t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    num = math.gcd(k, 100 - k)

    print(k // num + (100 - k) // num)