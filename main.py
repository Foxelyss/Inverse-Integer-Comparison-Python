import time
import matplotlib.pyplot as plt


def inverse_with_string(num=0):
    return int(str(num)[::-1])


def inverse_with_array(num):
    array = []
    while num > 0:
        array.append(num % 10)
        num //= 10

    inversed = 0

    for x in range(1, len(array) + 1):
        inversed += array[-x] * 10 ** (x - 1)

    return inversed


def inverse_with_math(num):
    inversed = 0

    while num > 0:
        inversed *= 10
        inversed += num % 10
        num //= 10

    return inversed


def measure_time(func, value):
    start = time.monotonic_ns()

    func(value)

    finish = time.monotonic_ns()

    time_in_ns = (finish - start)
    return time_in_ns


def measure_avarage_time(func, value):
    time = 0
    for x in range(10):
        time += measure_time(func, value)
    return time / 10


value = int(input("Введите первоначальное натуральное число: "))
value_on_start = value
print(f"Для числа: {value}")
print()

inverse_with_array_time = measure_avarage_time(inverse_with_array, value)
print("Инвертирование с массивом")
print(f'Среднее время работы в наносекундах: {inverse_with_array_time}')

inverse_with_string_math = measure_avarage_time(inverse_with_string, value)
print()
print("Строчное инвертирование")
print(f'Среднее время работы в наносекундах: {inverse_with_string_math}')

inverse_with_math_time = measure_avarage_time(inverse_with_math, value)
print()
print("Математическое инвертирование")
print(f'Среднее время работы в наносекундах: {inverse_with_math_time}')

array_invert_avarages = []
string_invert_avarages = []
math_invert_avarages = []

step = 25

while value < 10 ** 15:
    array_invert_avarages.append(measure_avarage_time(inverse_with_array, value))
    string_invert_avarages.append(measure_avarage_time(inverse_with_string, value))
    math_invert_avarages.append(measure_avarage_time(inverse_with_math, value))
    value *= step

plt.plot(array_invert_avarages, '-o', label="Инвертирование с массивом")
plt.plot(string_invert_avarages, '-o', label="Строчное инвертирование")
plt.plot(math_invert_avarages, '-o', label="Математическое инвертирование")
plt.ylabel('Время (наносек.)')
plt.annotate("", xy=(0, string_invert_avarages[0]), xytext=(-0.1, -0.2),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel(f'Величина числа от {value_on_start} до 10 в 15 степени, шагом умножения {step}')
plt.legend()
plt.show()
