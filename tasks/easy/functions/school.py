"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""


def incr_students(arg1: dict, arg2):
    arg1[arg2] = arg1.get(arg2) + 1


def decr_students(arg1: dict, arg2):
    if arg1.get(arg2) > 0:
        arg1[arg2] = arg1.get(arg2) - 1
    else:
        print("Количество учеников в классе должно быть больше 0")


def add_class(arg1: dict, arg2):
    arg1.update({arg2: 0})


def remove_class(arg1: dict, arg2):
    del arg1[arg2]


def calc_students(class_list: dict):
    return print(sum(class_list.values()))


if __name__ == '__main__':
    school_data = {
        '1a': 15,
        '1b': 23,
        '2a': 13,
        '2b': 30
    }

    print(school_data)
    incr_students(school_data, '1a')
    decr_students(school_data, '1b')
    add_class(school_data, '3a')
    remove_class(school_data, '2a')
    calc_students(school_data)
    print(school_data)
