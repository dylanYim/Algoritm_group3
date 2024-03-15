nums = []
count = int(input())

for i in range(count):
    num1, num2 = input().split()
    
    num1 = int(num1)
    num2 = int(num2)

    nums.append(num1 + num2)

for i in range(count):
    print (nums[i])