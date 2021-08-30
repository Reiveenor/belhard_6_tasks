"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(arg1: int):
    if arg1 & (arg1 - 1) == 0:
        return print(True)
    else:
        return print(False)


if __name__ == '__main__':
    check_number(16)
