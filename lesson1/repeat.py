# Декораторы

def info(func):
    def _f():
        func()

    return _f

@info
def sum1(num1, num2):
    return num1 + num2


sum1(1, 2)

