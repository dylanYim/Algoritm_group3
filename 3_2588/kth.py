num1 = int(input())
num2 = int(input())

num2_list = []
for i in str(num2):
    num2_list.append(i)

print(num1 * int(num2_list[2]))
print(num1 * int(num2_list[1]))
print(num1 * int(num2_list[0]))
print(num1 * num2)