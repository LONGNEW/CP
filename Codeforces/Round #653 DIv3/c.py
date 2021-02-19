import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    string = list(sys.stdin.readline().strip())
    left = 0
    right = 0
    for item in string:
        if item == '(':
            left += 1
        else:
            if left > 0:
                left -= 1
            right += 1
    print(left)