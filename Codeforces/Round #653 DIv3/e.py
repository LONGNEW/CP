import sys

n, k = map(int, sys.stdin.readline().split())
two_like = []
bob_like = []
alice_like = []

for i in range(n):
    t, a, b = map(int, sys.stdin.readline().split())
    if a == 1 and b == 1:
        two_like.append([t, a, b])
    elif b == 1:
        bob_like.append([t, a, b])
    elif a == 1:
        alice_like.append([t, a, b])

two_like.sort()
bob_like.sort()
alice_like.sort()

time = 0
cnt = 1
two_like_idx = 0
one_like_idx = 0
while two_like_idx < len(two_like) - 1 and one_like_idx < min(len(bob_like), len(alice_like)):

    if two_like[two_like_idx][0] < bob_like[one_like_idx][0] + alice_like[one_like_idx][0]:
        time += two_like[two_like_idx][0]
        cnt += 1
        two_like_idx += 1
    else:
        time += bob_like[one_like_idx][0] + alice_like[one_like_idx][0]
        cnt += 1
        one_like_idx += 1

if cnt < k:
    print(-1)
else:
    print(cnt)
