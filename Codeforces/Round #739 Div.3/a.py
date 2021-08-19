import sys

temp = []
for i in range(1, 2000):
    if i % 3 == 0:
        continue

    if str(i)[-1] == '3':
        continue

    temp.append(i)

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    print(temp[k - 1])