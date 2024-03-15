t = int(input())
ans = []
for _ in range(t):
    a, b = input().split()
    a = int(a)
    ch = []
    for i in range(len(b)):
        for j in range(a):
            ch.append(b[i])
    s = ''.join(ch)
    ans.append(s)

for c in ans:
    print(c)