import sys

x = list(map(int, sys.stdin.readline().strip()))
m = int(sys.stdin.readline())

start = max(x) + 1
end = 10 ** 18

# 어떤 진법을 쓰든 1의 자리는 관련이 없다.
# 길이가 1일때는 예외적으로 처리해주자.
if len(x) == 1:
    print(1 if x[0] <= m else 0)
    exit()

while start <= end:
    mid = (end + start) // 2
    base = [0] * (len(x))

    for i in range(len(x)):
        idx = len(x) - 1 - i
        base[i] = mid ** idx

    temp = 0
    for i in range(len(x)):
        temp += x[i] * base[i]

    if temp <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end - max(x))
