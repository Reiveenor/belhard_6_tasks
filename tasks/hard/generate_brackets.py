"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def generate_basket(n, sequence="", opened=0, closed=0):
    if len(sequence) != n * 2:
        if opened < n:
            generate_basket(n, sequence + "(", opened + 1, closed)
        if closed < opened:
            generate_basket(n, sequence + ")", opened, closed + 1)
    else:
        print(sequence)


if __name__ == '__main__':
    generate_basket(4)
