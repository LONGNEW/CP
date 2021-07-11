import sys

n, t = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

left, right = 1, n
while left <= right:
    mid = (left + right) // 2
    print(f"? {1} {mid}")
    sys.stdout.flush()

    total = mid - int(sys.stdin.readline())

    if total >= k:
        right = mid - 1
    else:
        left = mid + 1

print(f"! {left}")