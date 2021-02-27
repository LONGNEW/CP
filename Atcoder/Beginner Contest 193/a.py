import sys

a, b = map(int, sys.stdin.readline().split())
num = a - b
print((num / a) * 100)