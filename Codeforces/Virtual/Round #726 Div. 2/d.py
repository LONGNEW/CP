import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    if n % 2 == 1:
        print("Bob")
    else:
        if math.log2(n) == int(math.log2(n)):
            if int(math.log2(n)) % 2 == 1:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Alice")