import sys
trial = int(sys.stdin.readline())

list1_str = input()
list1 = list1_str.split()

for i in range(len(list1)):
    list1[i] = int(list1[i])

def perm(lst,n):
	ret = []
	if n > len(lst): return ret

	if n==1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)):
			temp = [i for i in lst]
			temp.remove(lst[i])
			for p in perm(temp,n-1):
				ret.append([lst[i]]+p)

	return ret


sum_max = 0
sum_temp = 0
for i in perm(list1, trial):
    for j in range(len(i)-1):
        sum_temp += abs(i[j+1] - i[j])
    if sum_temp > sum_max:
        sum_max = sum_temp
    sum_temp = 0
print(sum_max)
			

print(sum)