def is_divisible_by_three(number):
    if(number % 3 == 0):
       print("Число делится на 3")
    else:
        print("Число не делится на 3")

number = int(input("Введите число"))

print(is_divisible_by_three(number))