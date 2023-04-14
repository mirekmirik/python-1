#1 завдання

num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

if num1 > num2:
    print(num1, "більше за", num2)
elif num1 < num2:
    print(num2, "більше за", num1)
else:
    print("Обидва числа рівні") 
    
#3 завдання

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

result = 0

for i in range(num2):
    result += num1

print("Результат множення:", result)

#4 завдання

dividend = int(input("Введіть ділене: "))
divisor = int(input("Введіть дільник: "))

quotient = 0

while dividend >= divisor:
    dividend -= divisor
    quotient += 1

print("Результат цілочисельного ділення:", quotient)
