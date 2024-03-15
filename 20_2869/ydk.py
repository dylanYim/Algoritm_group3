a, b, v = map(int,input().split())
day = 1
while True:
    v -= a
    if v <= 0:
        break
    v += b
    day +=1
print(day)

