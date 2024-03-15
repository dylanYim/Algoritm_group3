a = int(input())
b = int(input())
c = int(input())

result = a * b * c
num_list = list(str(result))

print(num_list)

for i in range(10):
    count = num_list.count(str(i))
    print(count)
