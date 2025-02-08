# Завдання 1

# Напишіть скрипт, який створює текстовий файл і записує до нього
# 10000 випадкових дійсних чисел. Створіть ще один скрипт,
# який читає числа з файлу та виводить на екран їхню суму.

import random

numbers = [random.randint(1, 1000) for _ in range(10000)]

with open("numbers.txt", "w") as file_obj:
    for number in numbers:
        file_obj.write(str(number) + "\n")

try:
    total = 0
    with open("numbers.txt", "r") as file_obj:
        for num in file_obj:
            total += int(num.strip())
    print(total)
except FileNotFoundError:
    print("Файл ще не створено!")
