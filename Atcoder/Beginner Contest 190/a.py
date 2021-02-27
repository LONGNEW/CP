import sys

a, b, c = map(int, sys.stdin.readline().split())

print("Takahashi" if a + c > b else "Aoki")