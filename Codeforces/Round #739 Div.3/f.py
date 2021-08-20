import bisect

data = set()
c = "0123456789"

for i in c:
    for j in c:
        z = set()
        z.add(i)
        z.add(j)
        temp = [i, j]

        for k in temp:

            if k + i not in z:
                z.add(k + i)
                temp += [k + i]

            if k + j not in z:
                z.add(k + j)
                temp += [k + j]

            if len(k) > 10:
                break

        data = data.union(z)

k1, k2 = [], []
for item in data:
    if len(set(item)) == 1:
        k1.append(item)
    else:
        k2.append(item)

k1 = sorted(map(int, k1))
k2 = sorted(map(int, k2))

for i in range(int(input())):
    n, k = map(int, input().split())
    q = set(str(n))

    if len(q) > k:
        if k == 1:
            print(k1[bisect.bisect(k1, n)])
        else:
            print(k2[bisect.bisect(k2, n)])
    else:
        print(n)