from itertools import permutations

num_list = []
i_arr = []
card = int(input())
deck = int(input())

for _ in range(card):
    num_list.append(int(input()))

arr = list(permutations(num_list, deck))

for i in range(len(arr)):
    i_arr.append(''.join(map(str, arr[i])))
i_arr = list(set(i_arr))
print(len(i_arr))