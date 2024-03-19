def perm(lst,n):
	ret = []
	if n > len(lst): return ret

	if n == 1:
		for i in lst:
			ret.append([i])
	elif n > 1:
		for i in range(len(lst)):
			temp = [i for i in lst]
			temp.remove(lst[i])
			for p in perm(temp,n-1):
				ret.append([lst[i]]+p)

	return ret


import sys
trial = int(sys.stdin.readline())
n = int(sys.stdin.readline())
list1 = []

while trial > 0:
	list1.append(int(sys.stdin.readline()))
	trial -= 1

created_numbers = []
word = str("")

for i in perm(list1, n):
	for j in range(len(i)):
		word += str(i[j])

	word = int(word) # 이거 없어도 되는데, 있으니까 더 빠르다. 왜?

	if word not in created_numbers:
		created_numbers.append(word)

	word = str("")

print(len(created_numbers))
		