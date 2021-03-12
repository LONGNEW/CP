import sys

temp = sys.stdin.readline().strip()
ans = 0

while True:
    temp = sys.stdin.readline().strip()

    if temp == "고무오리 디버깅 끝":
        break

    if temp == "고무오리":
        if ans == 0:
            ans += 2
        else:
            ans -= 1
    else:
        ans += 1

print("고무오리야 사랑해" if ans == 0 else "힝구")