import sys
trial = 9
list1 = []
while trial > 0:
	list1.append(int(sys.stdin.readline()))
	trial -= 1

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


for i in comb(list1, 7):
	if sum(i) == 100:
		i.sort()
		for j in range(len(i)):
			print(i[j])
		break