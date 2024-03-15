lst=[]
for i in range(9):
    lst.append(int(input()))

a = max(lst)
b = lst.index(a)+1
print(a)
print(b)