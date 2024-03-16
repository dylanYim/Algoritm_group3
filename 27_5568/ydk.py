from itertools import combinations, permutations
n = int(input())
k = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

com = list(combinations(lst,k))
a = set()
for c in com:
    per = list(permutations(c,k))
    for p in per:
        v = ''.join(map(str,p))
        a.add(v)

print(len(a))