"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(n: int):
    fib1 = fib2 = 1
    print(fib1)
    print(fib2)
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2)


# raise StopIteration


if __name__ == '__main__':
    fibonacci(10)
