"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n: int):
    if n % 2 != 0:
        print(f"{n} is not degree 2, so it is False")
        return check_number(n // 2)
    else:
        return print(f"{n} is degree 2, so it is True")


if __name__ == '__main__':
    check_number(1)
