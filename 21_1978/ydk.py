n = int(input())
lst = map(int,input().split(' '))
ans = 0
for l in lst:
    if l == 1:
        continue
    is_prime = True
    for i in range(2, l):
        if l % i == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1
    else:
        is_prime = False

print(ans)