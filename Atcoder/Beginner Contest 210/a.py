import sys

n, a, x, y = map(int, sys.stdin.readline().split())

# cnt = 0
# ans = 0
# while cnt < n:
#     if cnt < a:
#         ans += x
#     else:
#         ans += y
#     cnt += 1
# print(ans)

print(a * x + (n - a) * y if n > a else n * x)