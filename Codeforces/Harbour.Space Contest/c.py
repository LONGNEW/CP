import sys

t = int(sys.stdin.readline())
for _ in range(t):
    data = sys.stdin.readline().rstrip()
    temp = []
    cnt = 0
    ans = 10

    for item in data:
        if item == '?':
            cnt += 1
        temp.append(item)

    for i in range(2 ** cnt):
        team = [0, 0]
        q = bin(i)[2:]

        question_idx = 0
        pre = ""
        for j in range(len(q), cnt):
            pre += "0"

        q = pre + q
        for idx in range(len(data)):
            if data[idx] == '?':
                temp[idx] = q[question_idx]
                question_idx += 1

            team[idx % 2] += int(temp[idx])

            if team[0] > team[1] + (len(data) - idx) // 2:
                ans = min(ans, idx + 1)

            if team[0] + (len(data) - 1 - idx) // 2 < team[1]:
                ans = min(ans, idx + 1)

    print(ans)