import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()

    left = data[:len(data) // 2]
    right = data[len(data) // 2:]
    ans = []
    for j in range(len(left)):
        ans.append(left[j])
        ans.append(right[j])
    print(*ans)
