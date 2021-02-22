import sys
from collections import Counter

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

cnt = -999
for i in range(len(data), 0, -1):
    word = data[:i]
    count = Counter(word)
    a = count.most_common()
    flag = 1

    for item, num in a:
        if num > k:
            flag = 0
            break

    if flag:
        cnt = max(cnt, len(word))

print(cnt)