import sys
from collections import defaultdict
import math

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    d = defaultdict(int)

    ans = []
    D, K = 0, 0

    for item in data:
        if item == 'D':
            D += 1
        if item == 'K':
            K += 1

        gcd = math.gcd(D, K)
        d[(D // gcd, K // gcd)] += 1
        ans.append(d[(D // gcd, K // gcd)])

    print(* ans)