import sys
trial = int(sys.stdin.readline())

lst = []

for i in range(trial):
    x = str(sys.stdin.readline()).strip()
    if (x) not in lst:
        lst.append(x)

lst.sort()
lst.sort(key=len)
    
for i in lst:
    print(i)


