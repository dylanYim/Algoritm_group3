num = int(input())
count = 0
if num < 100:
    count = num
else:
    count += 99
    for i in range(100, num+1):
        i = str(i)
        d = int(i[0]) - int(i[1])
        if d == int(i[1]) - int(i[2]):
            count += 1

print(count)