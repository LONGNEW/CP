import sys

string = sys.stdin.readline().strip()

flag = 1

for idx, item in enumerate(string):
    if idx % 2 == 1:
        if 97 <= ord(item) <= 122:
            flag = 0
    else:
        if 65 <= ord(item) <= 90:
            flag = 0

if flag:
    print("Yes")
else:
    print("No")