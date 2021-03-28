import sys

s = list(sys.stdin.readline().rstrip())
data = []
s.append(s[0])

for i in range(1, len(s)):
    print(s[i], end="")
