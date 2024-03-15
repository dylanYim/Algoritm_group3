import math
lst = list(map(int, input().split()))
print(min(lst[0]-0,lst[1]-0,lst[2]-0,lst[3]-0,abs(lst[0]-lst[2]),abs(lst[1]-lst[3])))