import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(sys.stdin.readline().rstrip())
    b = list(sys.stdin.readline().rstrip())
    a.append('1')
    b.append('1')
    cnt, flag = 0, 0

    for i in range(n):
        cnt += (a[i] == '1') - (a[i] == '0')

        if ((a[i] == b[i]) != (a[i + 1] == b[i + 1])) and cnt != 0:
            flag = 1
            break

    print("NO" if flag else "YES")