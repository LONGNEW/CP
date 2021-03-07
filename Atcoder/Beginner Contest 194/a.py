import sys

a, b = map(int, sys.stdin.readline().split())
solid = a + b
fat = b
if solid >= 15 and fat >= 8:
    print(1)
elif solid >= 10 and fat >= 3:
    print(2)
elif solid >= 3:
    print(3)
else:
    print(4)