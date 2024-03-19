import sys
a,b = map(str,sys.stdin.readline().split())

a1 = b1 = ""
for i in range(len(a)-1,-1,-1):
    a1 = a1 + str(a[i])

for i in range(len(b)-1,-1,-1):
    b1 = b1 + str(b[i])

a1 = int(a1)
b1 = int(b1)

if a1 > b1:
    print(a1)
else:
    print(b1)

