import sys

data = list(sys.stdin.readline().strip())
ans = []

for item in data:
    if item == "0":
        ans.append("0")
    elif item == "6":
        ans.append("9")
    elif item == "8":
        ans.append("8")
    elif item == "1":
        ans.append("1")
    else:
        ans.append("6")

ans.reverse()
print("".join(ans))