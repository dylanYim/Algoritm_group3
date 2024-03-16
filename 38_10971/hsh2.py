import sys
import itertools
trial = N = int(sys.stdin.readline())

cities = []


while trial > 0:
    list1_str = input()
    list1 = list1_str.split()
    for i in range(len(list1)):
        list1[i] = int(list1[i])
        if list1[i] == 0:
            list1[i] = 10000001
    cities.append(list1)

    trial -= 1


def dist(n, m):
    return cities[n][m] 

def solve(arrived, arr):
    global start
    ret = []
    if len(arr) == 1:
        return dist(arrived,arr[0]) + dist(arr[0], start)


    for i in range(len(arr)):
        new_arrived = arr[i]
        new_arr = arr[:i] + arr[i+1:]
        ret.append(dist(arrived, new_arrived)+solve(new_arrived, new_arr))
    
    return min(ret)


arr1 = []
for i in range(N):
    arr1.append(i)

for start in arr1:
    ret = []
    new_arr = arr1[:start] + arr1[start+1:]
    ret.append(solve(start,new_arr))
print(min(ret))