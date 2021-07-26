# from r-tron18's solution
import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()

    if data[0] < 0:
        print("no")
        continue

    print("yes")
    print("101")
    for j in range(0, 101):
        print(j, end=" ")
    print()