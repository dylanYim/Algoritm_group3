t = int(input())
lst = []
for _ in range(t):
    case = list(map(int, input().split(' ')))
    sum = 0
    for i in range(1,len(case)):
        sum += case[i]

    avg = round(sum / case[0],3)
    lst.append(avg)

for l in lst:
    print(l)