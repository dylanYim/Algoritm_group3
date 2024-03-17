from itertools import combinations
lst = []
for _ in range(9):
    lst.append(int(input()))

ans = []
dwarfs = list(combinations(lst,7))
for dwarf in dwarfs:
    sum = 0
    for d in dwarf:
        sum += d
    if sum == 100:
        ans = list(dwarf)
        break
ans.sort()
for a in ans:
    print(a)