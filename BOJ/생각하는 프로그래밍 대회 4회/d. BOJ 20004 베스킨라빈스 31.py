import sys

a = int(sys.stdin.readline())

ans = []
for i in range(1, a + 1):
    if 31 % (i + 1) == 1:
        ans.append(i)

for item in ans:
    print(item)