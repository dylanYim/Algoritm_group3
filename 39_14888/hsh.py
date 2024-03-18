import sys
trial = int(sys.stdin.readline())

numbers_str = input()
numbers = numbers_str.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

operator_str = input()
operator = operator_str.split()
for i in range(len(operator)):
    operator[i] = int(operator[i])



def perm(char, Kor, operator):

    global numbers, temp_sum, result

    if sum(operator) == 0:
        for i in range(len(numbers)-1):
            if i == 0:
                temp_sum = numbers[0]

            if char[i] == "합":
                temp_sum += numbers[i+1]
            elif char[i] == "차":
                temp_sum -= numbers[i+1]
            elif char[i] == "곱":
                temp_sum *=  numbers[i+1]
            elif char[i] == "몫":
                if temp_sum < 0:
                    temp_sum =  -1*((-1* (temp_sum)) // numbers[i+1])
                else:
                    temp_sum //=  numbers[i+1]
                    
            
        result.append(temp_sum)
        temp_sum = 0
                

    for j in range(len(operator)):
        if operator[j] > 0:
            operator[j] -= 1
            char = char + Kor[j]
            perm(char, Kor, operator)
            char = char[:-1]
            operator[j] += 1

Kor = ["합", "차", "곱", "몫"]
result = []
temp_sum = 0

perm("",Kor,operator)
print(max(result))
print(min(result))

