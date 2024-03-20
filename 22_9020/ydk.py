t = int(input())
lst = []
ans = []
for _ in range(t):
    lst.append(int(input()))

def get_prime_list(n):
    chae = [True] * n
    m = int(n**0.5)
    for i in range(2,m+1):
        if chae[i]:
            for j in range(i+i, n, i):
                chae[j] = False

    return [i for i in range(2,n) if chae[i]]

for l in lst:
    pans = []
    plst = get_prime_list(l)
    for p in plst:
        j = l-p
        if j in plst and j >= p:
            pans.append(str(p) + ' ' + str(j))
    ans.append(pans[-1])

for a in ans:
    print(a)

