from itertools import permutations
n = int(input())
lst = list(map(int, input().split()))

pers = list(permutations(lst))

def abs_sum(per):
    sum = 0
    for i in range(len(per)-1):
        sum += abs(per[i]-per[i+1])
    return sum

ans = 0
for per in pers:
    ans = max(ans,abs_sum(per))

print(ans)
