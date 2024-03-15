import sys
N = int(sys.stdin.readline())
cnt = 0
N = str(N)
for i in range(1, int(N)+1):
    if 1<=i<=99:
        cnt += 1
    else:
        i = str(i)
        list1 = []
        for j in range(0, len(i)-1):
            list1.append(int(i[j]) - int(i[j+1]))
        for k in range(0,len(list1)-1):
            if list1[k] != list1[k+1]:
                break
            else:
                cnt+=1

print(cnt)
        

