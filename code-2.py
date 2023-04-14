#2 завдання

def multiply(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + multiply(num1, num2-1)

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

result = multiply(num1, num2)

print("Результат множення:", result)

#3 завдання

def divide(dividend, divisor):
    if dividend < divisor:
        return 0
    else:
        return 1 + divide(dividend - divisor, divisor)

#Списки: 1 завдання

matrix = [
  [1, 4, 7],
  [21, 19, 5],
  [6, 11, 9]
]

elements = [elem for row in matrix for elem in row]
average = sum(elements) / len(elements)

odd_elements = list(filter(lambda x: x % 2 != 0, elements))
odd_sum = sum(odd_elements)

diag_product = 1
for i in range(len(matrix)):
  diag_product *= matrix[i][i]

print(f"Середнє арифметичне: {average}")
print(f"Сума непарних елементів: {odd_sum}")
print(f"Добуток елементів головної діагоналі: {diag_product}")

#Списки: 2 завдання

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

print("Найбільший спільний дільник чисел", a, "і", b, "дорівнює", gcd(a,b))
