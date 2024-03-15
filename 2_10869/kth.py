while True:
    num1 = input("첫번째 숫자 입력 (1이상): ")
    if num1.isdigit():
        num1 = int(num1)
        if 5 <= num1:
            break
        else: 
            print("조건에 맞는 숫자 입력")
    else: 
        print("숫자를 입력")

while True:
    num2 = input("두번째 숫자 입력 (10,000이하): ")
    if num2.isdigit():
        num2 = int(num2)
        if num2 <= 10000:
            break
        else:
            print("조건에 맞는 숫자 입력")
    else:
        print("숫자를 입력")  
        

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)