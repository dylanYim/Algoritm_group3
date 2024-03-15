x = int(input())
ans = 0
if x < 100:
    ans = x

if x < 1000:
    ans += 99
    for i in range(100, x+1):
        i = str(i)
        a, b, c = int(i[0]), int(i[1]), int(i[2])
        if 2*b == a+c:
            ans+=1

print(ans)