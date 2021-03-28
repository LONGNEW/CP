import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    one = []
    for item in data:
        one.append(item)
    two = []

    ans = 0
    for idx in range(len(data) - 1):
        temp = one[idx]
        min_idx = idx
        for k in range(idx, len(data)):
            if temp > one[k]:
                temp = one[k]
                min_idx = k

        temp_one = one[:idx]
        temp_two = one[idx:min_idx + 1]
        temp_two.reverse()
        temp_thr = one[min_idx + 1:]

        two = temp_one + temp_two + temp_thr
        one = []
        for idx, item in enumerate(two):
            one.append(item)

        ans += len(temp_two)

    print("Case #{}: {}".format(i + 1, ans))