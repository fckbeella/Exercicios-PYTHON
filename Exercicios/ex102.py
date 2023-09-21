from math import factorial
def fatorial(num=0, show=False or True):
    n = factorial(num)
    if show == False:
        print(n)
    else:
        while num > 0:
            print(f'{num}', end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(f' = {n}', end='')
            num -= 1
fatorial(5,show=True)