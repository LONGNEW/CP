import sys

x = sys.stdin.readline()

if x == "0":
    print(0)
else:
    data = x.split(".")
    print(data[0])