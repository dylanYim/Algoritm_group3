nums = []

while True:
    num = int(input())
    if (num >= 100):
        continue
    else:
        nums.append(num)
        if(len(nums) == 9):
            break

print(max(nums))
print(nums.index(max(nums))+1)