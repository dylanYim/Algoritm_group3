import sys
trial = int(sys.stdin.readline())

while trial > 0:
    list1_str=input()
    list1 = list1_str.split()
    for i in range(0, len(list1)):
        list1[i] = int(list1[i])
    sum = 0
    for i in range(1, len(list1)):
        sum += list1[i]
    avg = sum / list1[0]
    count = 0
    for i in range(1, len(list1)):
        if list1[i] > avg:
            count += 1
    prop = count / list1[0]
    print("{:.3f}%".format(prop*100))

    trial -= 1