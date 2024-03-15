import sys,math
trial = int(sys.stdin.readline())
list1_str=input()
list1 = list1_str.split()
cnt = 0

for i in list1:
    i = int(i)
    if i == 1:
        cnt +=1
    for j in range(2,int(math.sqrt(int(i)))+1):
        if i % j == 0:
            cnt += 1
            break
print(trial-cnt)