import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    univ = list(map(int, sys.stdin.readline().split()))
    skill = list(map(int, sys.stdin.readline().split()))
    schools = dict()

    for i in range(0, n):
        if univ[i] not in schools:
            schools[univ[i]] = [skill[i]]
        else:
            schools[univ[i]].append(skill[i])

    for item in schools.keys():
        schools[item].sort(key=lambda x:-x)
        prev = 0
        temp = []

        for skills in schools[item]:
            prev += skills
            temp.append(prev)

        schools[item] = temp

    ans = [0] * (n + 1)
    for item in schools.values():
        for i in range(1, len(item) + 1):
            remain = len(item) % i
            if remain == 0:
                ans[i] += item[-1]
            else:
                ans[i] += item[(-1-remain)]
    print(*ans[1:])
