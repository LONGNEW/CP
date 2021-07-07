import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()

    zeros = 0
    for item in data:
        if item == '0':
            zeros += 1

    if data == data[::-1]:
        if zeros == 1 or zeros % 2 == 0:
            print("BOB")
        else:
            print("ALICE")
    else:
        if zeros == 2 and len(data) % 2 == 1 and data[len(data) // 2] == '0':
            print("DRAW")
        else:
            print("ALICE")

