# from r-tron18's solution
import sys


def check():
    for j in range(26):
        word = chr(j + 97)
        if word not in data:
            return word

    for j in range(26):
        for k in range(26):
            word = chr(j + 97) + chr(k + 97)
            if word not in data:
                return word

    for j in range(26):
        for k in range(26):
            for l in range(26):
                word = chr(j + 97) + chr(k + 97) + chr(l + 97)
                if word not in data:
                    return word

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    print(check())