import sys
import math
N,M = map(int,sys.stdin.readline().split())

list1_str = input()
list1 = list1_str.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1.sort(reverse=True)

def cutting(lst, tree, depth = 1):
   if len(lst) == 1:
       return lst[0] - math.ceil(tree//depth)
   else:
        if (lst[0] - lst[1])* depth < tree :
           tree -= depth*(lst[0] - lst[1])
           return cutting(lst[1:], tree, depth+1)
        else:
           return lst[0] - math.ceil(tree//depth)



print(cutting(list1, M))
