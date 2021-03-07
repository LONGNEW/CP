import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))

data.sort(key=lambda x:x[0])
a = data[0]

data.pop(0)

data.sort(key=lambda x:x[1])
b = data[0]

if sum(a) > max(a[0], b[1]):
    print(max(a[0], b[1]))
else:
    print(sum(a))