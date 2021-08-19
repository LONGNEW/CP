import sys

def make(a, b, temp_str):
    if len(temp_str) > 0 and int(temp_str) not in numbers[len(temp_str)]:
        numbers[len(temp_str)].append(int(temp_str))

    if len(temp_str) == 9:
        return

    make(a, b, temp_str + str(a))
    make(a, b, temp_str + str(b))

numbers = [[] for _ in range(10)]

for i in range(1, 10):
    for j in range(i + 1, 10):
        make(i, j, "")

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    ans = 0

    for i in range(len(str(n)), 10):
        for item in sorted(numbers[i]):
            elements = 1

            for ch in str(item):
                if ch != str(item)[0]:
                    elements += 1
                    break

            if item >= n and elements == k:
                ans = item
                break
        if ans != 0:
            break

    print(ans)