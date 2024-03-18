import sys
trial = int(sys.stdin.readline())

lst = []

for i in range(trial):
    x = str(sys.stdin.readline()).strip()
    if [x,len(x)] not in lst:
        lst.append([x, len(x)])

lst.sort()

n = len(lst)
print(lst)
for i in range(1,n):
    j = i
    tmp = lst[i]
    while j > 0 and lst[j-1][1] > tmp[1]:
        lst[j] = lst[j-1]
        j -= 1
    lst[j] = tmp
    
for i in lst:
    print(lst[i])


