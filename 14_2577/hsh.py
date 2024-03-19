import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

abc = a*b*c
list1 = [0] * 10

while abc != 0:
    list1[abc % 10] += 1
    abc = abc // 10

for i in list1:
    print(i)
