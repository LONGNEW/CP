import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

count = [0] * n
for a in data[:m]:
    count[a] += 1

# 문제를 푸는 아이디어는 결국 그냥 배열을 다 찢어서 생각을 하는 건데.
# 각 count를 다 체크 해서 비어있으면 그게 정답이 되는 것이다.
for i in range(m):
    if count[i] == 0:
        ans = i
        break
# for - else 라는 문법이 존재한다.
# flag를 달던 것과 비슷한 문법으로,
# break 가 발생하지 않고 끝까지 수행 되었을 때 else가 실행된다.
else:
    ans = m

# 그렇게 0 ~ m 까지 했으니까
# 인제 각 lower, upper에다가 i를 더하면서 이 배열의 구성 원소를 바꾸는 것이다.
# 그렇게 했을 떄 인제 사라지는 원소 즉 i에 존재했던 거의 count에서 1을 빼준다.
# 나타난 횟수로 따지기 때문에 이 사라진 것의 count가 0이 되면 이 값이 ans 보다
# 작은지 비교한 후에 업데이트 해준다.
for i in range(n - m):
    out = data[i]
    new = data[m + i]

    count[out] -= 1
    count[new] += 1

    if count[out] == 0:
        ans = min(ans, out)
print(ans)