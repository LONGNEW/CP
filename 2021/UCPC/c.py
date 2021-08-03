import sys

a, d, k = map(int, sys.stdin.readline().split())
d /= 100
k /= 100
ans, lose, win, run_time = 0, 1, d, a

while win <= 1:
    ans += run_time * lose * win
    run_time += a
    lose *= (1 - win)
    win += win * k

win = 1
ans += run_time * lose * win
print(f"{ans:.7f}")