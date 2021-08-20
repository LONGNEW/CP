import sys

def counts(idx):
    temp = 0

    for item in ch.keys():
        temp += ch[item] // idx
        if ch[item] % idx != 0:
            return -1

        idx -= 1

    return temp

def check():
    temp_ans, removed = data[:ret], list(ch.keys())[::-1]
    t_len, already_remove = 0, set()

    for item in removed:
        for char in temp_ans:

            if char in already_remove:
                continue

            if t_len >= len(data) or char != data[t_len]:
                return -1

            t_len += 1
        already_remove.add(item)

    return 1

for _ in range(int(sys.stdin.readline())):
    data = sys.stdin.readline().rstrip()
    ch, possible = dict(), 1

    for item in data[::-1]:
        if item not in ch:
            ch[item] = 1
        else:
            ch[item] += 1

    ret = counts(len(list(ch.keys())))

    if ret == -1:
        print(-1)
        continue

    if check() == -1:
        print(-1)
    else:
        ans = "".join(list(ch.keys())[::-1])
        print(f"{data[:ret]} {ans}")