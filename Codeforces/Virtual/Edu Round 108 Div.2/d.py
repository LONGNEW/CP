import sys


def check(left, right):
    global ans
    temp = pre

    while left >= 0 and right < n:
        temp -= (a[left] - a[right]) * (b[left] - b[right])
        ans = max(ans, temp)
        left -= 1
        right += 1

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ans = pre = sum(a[i] * b[i] for i in range(n))

for i in range(n - 1):
    check(i, i + 1)
    check(i - 1, i + 1)
print(ans)