import sys

t = int(sys.stdin.readline())
for i in range(t):
    x, y, data = sys.stdin.readline().split()
    x = int(x)
    y = int(y)

    temp = data[0]
    ans = 0
    for j in range(1, len(data)):
        if data[j] == '?':
            if temp == 'C':
                if x < 0:
                    ans += x
                    temp = 'J'

            elif temp == 'J':
                if y < 0:
                    ans += y
                    temp = 'C'

            else:
                if x < 0 and y < 0:
                    if x < y:
                        ans += x
                        temp = 'J'
                    else:
                        ans += y
                        temp = 'C'
                elif x < 0:
                    ans += x
                    temp = 'J'
                elif y < 0:
                    ans += y
                    temp = 'C'
            continue

        if temp == 'C':
            if data[j] == 'J':
                ans += x
        elif temp == 'J':
            if data[j] == 'C':
                ans += y

        temp = data[j]

    print("Case #{}: {} ".format(i + 1, ans))