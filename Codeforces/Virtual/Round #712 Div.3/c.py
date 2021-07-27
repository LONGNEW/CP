import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    cnt_one = 0
    for i in data:
        if i == '1':
            cnt_one += 1

    if data[0] == '0' or data[-1] == '0' or cnt_one % 2 == 1:
        print("NO")
        continue

    fir_ans, sec_ans = "", ""
    idx, record = 0, 1
    for i in range(n):
        if data[i] == '1':
            fir_ans += ')' if 2 * idx >= cnt_one else '('
            sec_ans += fir_ans[-1]
            idx += 1
        else:
            fir_ans += ')' if record == 1 else '('
            sec_ans += '(' if record == 1 else ')'
            record = -record

    print("YES")
    print(fir_ans)
    print(sec_ans)
