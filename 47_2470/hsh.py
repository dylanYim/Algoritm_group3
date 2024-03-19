import sys
trial = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
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
    else:
        left = left + 1

print(list1[answer_left], list1[answer_right])
