import sys
trial = int(sys.stdin.readline())

list1 = []
stop = temp = -1

while trial > 0:
    n = int(sys.stdin.readline())

    if len(list1) == 0:
        list1.append(n) 
    else:
        for i in range(len(list1)):
            if n >= list1[i]:
                if i == len(list1)-1:
                    list1.append(n)
                continue  # 없어도 되지만 있는게 빠름
            else:
                stop = i
                break

    if stop != temp:
        list1.append(None)
        for i in range(len(list1)-2, i-1, -1):
            list1[i+1] = list1[i]
        list1[stop] = n
        stop = -1
        
    trial -= 1

for i in list1:
    print(i)
