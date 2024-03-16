import sys
trial = int(sys.stdin.readline())
list1=[None] * trial

for i in range(trial):
    list1[i] = int(sys.stdin.readline())

def q_sort(arr, left, right):
    mid = (left + right) //2
    pivot = arr[mid]

    p_left = left
    p_right = right

    while p_left <= p_right:
        while arr[p_left] < pivot:
            p_left += 1
        while arr[p_right] > pivot:
            p_right -= 1
        
        if p_left <= p_right:
            arr[p_right], arr[p_left] = arr[p_left], arr[p_right]
            p_left += 1
            p_right -= 1
    
    if left < p_right:
        q_sort(arr, left, p_right)
    if p_left < right:
        q_sort(arr,  p_left, right)
        


q_sort(list1, 0, len(list1)-1)



for _ in list1:
    print(_)

    