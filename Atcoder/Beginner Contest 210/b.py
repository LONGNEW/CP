import sys

n = int(sys.stdin.readline())
data = sys.stdin.readline().rstrip()

now = True
for i in range(len(data)):
    if data[i] == '1':
        break
    now = not now

print("Takahashi" if now else "Aoki")