import sys, math

def check():
    visit = set()

    for i in range(len(num)):
        now = int(num[i])

        if now in visit:
            continue

        visit.add(now)
        for j in range(2, int(math.sqrt(now)) + 1):
            if now % j == 0:
                return now

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            now = int(num[i] + num[j])

            if now in visit:
                continue

            visit.add(now)
            for k in range(2, int(math.sqrt(now)) + 1):
                if now % k == 0:
                    return now

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = sys.stdin.readline().rstrip()
    num = []

    for item in n:
        num.append(item)

    if '1' in num:
        print(1)
        print(1)
        continue

    ans = check()
    print(len(str(ans)))
    print(ans)

