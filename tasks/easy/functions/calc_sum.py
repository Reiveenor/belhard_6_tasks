"""
Написать функцию calc_sum, которая принимает неограниченное количество целых
чисел и возвращает их сумму

для расчета суммы можно воспользоваться функцией sum
"""


def calc_sum(x: int):
    num_list = []
    while True:
        try:
            num_list.append(x)
            x = int(input("Введите целые числа: "))
            if type(x) != int:
                print("Числа не были введены, сумма = 0")
            break
        except ValueError:
            break
    return print(sum(num_list))


if __name__ == '__main__':
    print("Для завершения ввода нажмите любою букву")
    calc_sum(int(input("Введите целые числа: ")))
