"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n):
    def closure(x):
        num = int(x) * int(n)
        return print(num)
    return closure


if __name__ == '__main__':
    mul = multiply(input("n is: "))
    mul(input("x is: "))
