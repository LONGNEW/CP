import sys

n = sys.stdin.readline().strip()
if int(n) == 1:
    print(0)
    exit()

one = n[:len(n) // 2]
two = n[len(n) // 2:]

if int(two) == 0:
    ans = ""
    for i in range(len(two) - 1):
        ans += "9"
    print(int(ans))

elif len(one) != len(two):
    ans = ""
    for i in range(len(one)):
        ans += "9"
    print(int(ans))

elif int(one) > int(two):
    print(int(one) - 1)
else:
    print(int(one))
