n, l = input().split()
n = int(n)
l = int(l)
score = input().split()

for i in range(len(score)):
    score[i] = int(score[i])

for i in range(l):
    op, a, b = input().split()
    a = int(a)
    b = int(b)
    if op == "U":
        score[a-1] = b
    if op == "Q":
        if a > b:
            a, b = b, a
        elif a == b:
            print(score[a])
            continue

        print(max(score[a - 1:b]))
