
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

numbers = [num1, num2, num3]

ascending_order = sorted(numbers)
print("Числа в порядке возрастания:", ascending_order)

descending_order = sorted(numbers, reverse=True)
print("Числа в порядке убывания:", descending_order)
