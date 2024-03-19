import sys
N, M = map(int,sys.stdin.readline().split())
list1 = list(map(int, sys.stdin.readline().split()))

def comb(lst,n):
	ret = []
	if n > len(lst): return ret
	
	if n == 1:
		for i in lst:
			ret.append([i])
	elif n > 1:
		for i in range(len(lst)-n+1):
			for temp in comb(lst[i+1:],n-1):
				ret.append([lst[i]]+temp)

	return ret


max = 0
for i in comb(list1, 3):
	if sum(i) <= M and sum(i) > max:
		max = sum(i)

print(max)