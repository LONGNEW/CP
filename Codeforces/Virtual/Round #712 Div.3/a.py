import sys

def check():
    for i in range(len(data)):
        if 'a' != data[compare_idx - i]:
            return data[:i] + 'a' + data[i:]
    return -1

t = int(sys.stdin.readline())
for _ in range(t):
    data = sys.stdin.readline().rstrip()
    compare_idx = len(data) - 1

    ans = check()
    if ans == -1:
        print("NO")
    else:
        print("YES")
        print("".join(ans))
