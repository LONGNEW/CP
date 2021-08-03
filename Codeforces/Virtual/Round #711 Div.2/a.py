import sys
import math

def check(num):
    while True:
        temp, temp_ans = num, 0

        while temp > 0:
            temp_ans += temp % 10
            temp //= 10

        ans = math.gcd(num, temp_ans)
        if ans > 1:
            return num
        num += 1

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(check(n))