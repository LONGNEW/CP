import sys

for _ in range(int(sys.stdin.readline())):
    big = sys.stdin.readline().rstrip()
    small = sys.stdin.readline().rstrip()

    if len(small) > len(big):
        temp = small
        small = big
        big = temp

    words = set()
    length = len(small)
    for now in range(length, 0, -1):
        for start in range(len(small) - now + 1):
            words.add(small[start:start + now])

    pivot = len(big) + len(small)
    ans = float('inf')
    for item in words:
        if item in big and pivot - len(item) * 2 < ans:
            ans = pivot - len(item) * 2

    print(pivot if ans == float('inf') else ans)

