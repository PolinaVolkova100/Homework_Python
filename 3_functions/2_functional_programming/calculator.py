def zero(func=None):
    if func is None:
        return 0
    else:
        return func(0)


def one(func=None):
    if func is None:
        return 1
    else:
        return func(1)


def two(func=None):
    if func is None:
        return 2
    else:
        return func(2)


def three(func=None):
    if func is None:
        return 3
    else:
        return func(3)


def four(func=None):
    if func is None:
        return 4
    else:
        return func(4)


def five(func=None):
    if func is None:
        return 5
    else:
        return func(5)


def six(func=None):
    if func is None:
        return 6
    else:
        return func(6)


def seven(func=None):
    if func is None:
        return 7
    else:
        return func(7)


def eight(func=None):
    if func is None:
        return 8
    else:
        return func(8)


def nine(func=None):
    if func is None:
        return 9
    else:
        return func(9)


def plus(digit):
    def func(num):
        return digit + num

    return func


def minus(digit):
    def func(num):
        return num - digit

    return func


def times(digit):
    def func(num):
        return num * digit

    return func


def divided_by(digit):
    def func(num):
        return num // digit

    return func
