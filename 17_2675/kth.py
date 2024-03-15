r, s = input().split(' ')
r = int(r)
p = list(s)

for i in range(len(p)):
    for j in range(r):
        print(p[i], end="")