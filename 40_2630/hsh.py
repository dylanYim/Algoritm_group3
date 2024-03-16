import sys
lst = []
trial = N = int(sys.stdin.readline())
while trial > 0:
    list1_str = input()
    list1 = list1_str.split()
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    lst.append(list1)
    trial -= 1

blue_cnt = 0
white_cnt = 0
def func(lst, N):
    global white_cnt, blue_cnt
    flag = 0

    if N == 1:
        if lst[0][0] == 1:
            blue_cnt += 1
        else:
            white_cnt += 1
        return
    
    for i in range(N):
        for j in range(N):
            if lst[i][j] != lst[0][0]:
                flag = 1
                break
        if flag == 1:
            break


    if flag == 1:
    
        list1 = lst[:N//2]
        for j in range(len(list1)):
            list1[j] = list1[j][:N//2]
        func(list1, N//2)


        list2 = lst[:N//2]
        for j in range(len(list2)):
            list2[j] = list2[j][N//2:]
        func(list2, N//2)

        list3 = lst[N//2:]
        for j in range(len(list3)):
            list3[j] = list3[j][:N//2]
        func(list3, N//2)

        list4 = lst[N//2:]
        for j in range(len(list4)):
            list4[j] = list4[j][N//2:]
        func(list4, N//2)

    elif flag == 0:
        if lst[0][0] == 1:
            blue_cnt += 1
        else:
            white_cnt += 1

func(lst,N)
print(white_cnt)     
print(blue_cnt)
    
