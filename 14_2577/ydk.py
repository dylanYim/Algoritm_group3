a = int(input())
b = int(input())
c = int(input())

lst = [0]*10
chr = str(a*b*c)
for i in range(len(chr)):
    lst[int(chr[i])] += 1
for l in lst:
    print(l)