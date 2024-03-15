a = int(input())
b = input()
b = b[::-1]
lst = []
for i in range(len(b)):
    if i == 0:
        lst.append(a * int(b[i]))
    else:
        c = str(a * int(b[i]))
        lst.append(int(c[:len(c-1)]))
lst.append(a*b)

for l in lst:
    print(l)

