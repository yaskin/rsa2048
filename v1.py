# pip install sympy gmpy2
# pip install tqdm
#Два наибольших делителя числа 25212631813509849273: 4696934183 и 5367891231
#Среднее время выполнения операции: 225.23 сек
import time
from tqdm import tqdm

result_global = None

def calculate_timings(number):
    timings = []
    for i in range(5):
        start_time = time.time()

        num = int(number)
        square_root = int(num**0.5)
        print(f"Квадратный корень числа {num} равен: {square_root}")

        divisor1 = 1
        for j in tqdm(range(square_root, 1, -1), desc="Поиск делителей", unit="%", ncols=100):
            print(f"Делитель: {j}")
            if num % j == 0:
                divisor1 = j
                break

        divisor2 = num // divisor1

        end_time = time.time()
        execution_time = end_time - start_time
        timings.append(execution_time)

    average_time = sum(timings) / len(timings)

    return divisor1, divisor2, average_time

def find_largest_divisors(number):
    global result_global
    result_global = calculate_timings(number)
    print("Подсчет времени выполнения операции завершен. Для выполнения запроса вызовите функцию execute_query()")

def execute_query():
    global result_global
    if result_global is None:
        print("Сначала необходимо рассчитать время выполнения операции.")
    else:
        print(f"Два наибольших делителя числа: {result_global[0]} и {result_global[1]}")
        print(f"Среднее время выполнения операции: {result_global[2]:.2f} сек")

# Пример использования функций
number = "25212631813509849273"  # Очень большое число
find_largest_divisors(number)
execute_query()
