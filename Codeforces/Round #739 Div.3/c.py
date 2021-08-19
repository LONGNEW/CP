import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    target_range = 1

    if k == 1:
        print(f"1 1")
        continue

    while k > target_range * target_range:
        target_range += 1

    target_range -= 1
    start, end = target_range ** 2 + 1, (target_range + 1) ** 2
    middle = (end + start) // 2

    #fixed number target_range + 1
    if k < middle:
        print(f"{target_range + 1 - abs(middle - k)} {target_range + 1}")
    else:
        print(f"{target_range + 1} {target_range + 1 - abs(middle - k)}")