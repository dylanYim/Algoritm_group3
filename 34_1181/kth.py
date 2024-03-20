n = int(input())
lst = []
for _ in range(n):
    word = input()
    lst.append(word)

lst = list(set(lst))
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)