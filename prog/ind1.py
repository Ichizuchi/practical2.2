def number_to_words(number):
    number_words = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть"]
    if number < 0 or number > 6:
        return "Invalid Number"
    return number_words[number]


n = int(input("Введите натуральное число: "))
r = n % 7
k = (n - r) // 7
r_in_words = number_to_words(r)
print(f'n = 7k + {r_in_words}, where k = {k}')
