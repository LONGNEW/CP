import sys

limit = 10000001
temp = [0] * limit

for i in range(1, limit):
    if temp[i] != 0:
        continue

    temp[i] = i
    # finding all the square number
    j = 1
    while i * j * j <= limit:
        temp[i * j * j] = i
        j += 1

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))

    # if they have same number in temp list
    # then if you multiply this two you'll get square number
    # because they have same counts of number and trigger number(index i)
    # will be multiply twice so it will be square number

    now = set()
    cnt = 1
    for item in data:
        if temp[item] in now:
            now = set()
            cnt += 1

        now.add(temp[item])

    print(cnt)