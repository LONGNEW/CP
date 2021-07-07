import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    cnt = 0

    for item in data:
        if item == '0':
            cnt += 1
    if cnt == 1 or cnt % 2 == 0:
        print("BOB")
    else:
        print("ALICE")