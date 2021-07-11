import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    stars = []
    ans = 0

    for idx, item in enumerate(data):
        if item == '*':
            stars.append(idx)

    if not stars:
        print(0)
        continue

    target = stars[len(stars) // 2]
    
    left_pos = target - 1
    right_pos = target + 1

    left_star = len(stars) // 2 - 1
    right_star = len(stars) // 2 + 1

    while left_star >= 0:
        ans += left_pos - stars[left_star]
        left_star -= 1
        left_pos -= 1

    while right_star < len(stars):
        ans += stars[right_star] - right_pos
        right_star += 1
        right_pos += 1

    print(ans)