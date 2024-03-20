import sys
trial = int(sys.stdin.readline())
lst = []

while trial > 0:
    x = int(sys.stdin.readline())
    if x == 0:
        del lst[-1]
    else:
        lst.append(x)

    trial -= 1
print(sum(lst))