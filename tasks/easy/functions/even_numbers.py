"""
Написать функцию get_even_number, которая принимает 1 аргумент - номер
четного числа и возвращает само четное число

Например:

- get_even_number(10) -> 20
- get_even_number(3) -> 6
"""


def get_even_number(num: int):
    if int(num):
        number = num * 2
        return print(number)
    else:
        raise TypeError


if __name__ == '__main__':
    print("Input number: ")
    get_even_number(int(input()))
