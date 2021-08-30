import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

ans, cur_open = 0, 0
s = [[0, 0]]

for i in range(0, n, 2):
    if i + 1 >= n:
        continue

    open_bracket = data[i]
    close_bracket = data[i + 1]

    cur_open += open_bracket - close_bracket
    # 여기에 s[0][0]가 있어야 하는 이유가 만약 마지막에 찾았던 ')' 괄호가
    # 여는 괄호보다 많은 경우에 새로 시작되는 regular 괄호의 시작이
    # s[0][0]에 저장을 한다. 그리고 cur_open도 여기를 기준으로 움직인다.
    ans += min(close_bracket, cur_open + close_bracket - s[0][0])

    # 스택의 0번쨰에는 괄호의 개수가 있다.
    # 현재까지 닫는 괄호의 개수를 기준으로 본다고 보면 되는데 이전보다 적어진
    # cur_open이 온다는 것은 닫는 괄호가 더 많아짐을 의미한다.
    # 즉 이전에는 여는 괄호가 많았던 것이 닫을 수 있어졌다는 거다.
    # 현재를 기준으로 이전의 괄호를 찾는 것이기때문에 생각의 전환이 필요
    while s and s[-1][0] > cur_open:
        ans += s[-1][1]
        s.pop()

    # 동일한 경우에는 붙일 수 있는 거다.
    # 만약 1 1 1 1 1 9
    # 같은 것의 경우에는 여기를 두 번 거쳐서 [1]에는 2가 들어 있을 거다.
    if s and s[-1][0] == cur_open:
        ans += s[-1][1]
        s[-1][1] += 1
    else:
        # 길이가 존재한다는 거는 아직 새로운 괄호가 생기기 전이고
        # 존재하지 않는 것은 현재 닫는 괄호가 더 많았다는 의미이다.
        # 현재의 인덱스가 나타내는 닫는 괄호를 통해 새로운 정규식을 만들 수 있는 지를
        # 보기 때문에 1을 넣어서 만약 얘를 제대로 닫을 수 있다면 을 보는 것이다.
        if s:
            s.append([cur_open, 1])
        else:
            s.append([cur_open, 0])

print(ans)