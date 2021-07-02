import sys

n, q = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()
data = [0] * (len(s) + 1)

for i in range(len(s)):
    data[i + 1] = data[i] + ord(s[i]) - 96

for i in range(q):
    l, r = map(int, sys.stdin.readline().split())
    print(data[r] - data[l - 1])