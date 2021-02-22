import sys

n, m = map(int, sys.stdin.readline().split())
data = dict()
for i in range(n):
    word = sys.stdin.readline().strip()
    if data.get(word):
        data[word] += 1
    else:
        data[word] = 1

a = []
for item in data.keys():
    a.append((item, data[item], len(item)))

a.sort(key=lambda x:(-x[1], -x[2], x[0]))

for item, num, length in a:
    if length >= m:
        print(item)