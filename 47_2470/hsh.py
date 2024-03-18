import sys
trial = int(sys.stdin.readline())

list1_str = sys.stdin.readline()
list1 = list1_str.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])

list1.sort()

left, right = 0, trial-1
answer = abs(list1[left] + list1[right])
answer_left = left
answer_right = right

while left < right:
    result = list1[left] + list1[right]
    if result == 0:
        answer_left = left
        answer_right = right
        break

    if abs(result) < answer:
        answer = abs(result)
        answer_left = left
        answer_right = right

    if result > 0:
        right = right -1
    elif result < 0:
        left = left + 1



print(list1[answer_left], list1[answer_right])
