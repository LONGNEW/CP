import sys

data = dict()
ans = ["ABC", "ARC", "AGC", "AHC"]

for _ in range(3):
    data[sys.stdin.readline().rstrip()] = 1

for item in data.keys():
    idx = ans.index(item)
    ans.pop(idx)

print(ans[0])