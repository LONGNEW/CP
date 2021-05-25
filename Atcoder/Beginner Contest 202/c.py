import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

# 이 인덱스가 나타나는 횟수를 저장해놓음
appear = [0] * n
for item in c:
    appear[item - 1] += 1

data = dict()
for idx, item in enumerate(b):
    if item in data:
        data[item] += appear[idx]
    else:
        data[item] = appear[idx]

cnt = 0
for item in a:
    if item in data:
        cnt += data[item]

print(cnt)