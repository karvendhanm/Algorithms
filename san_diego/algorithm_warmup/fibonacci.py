# Uses python3

def calc_fib(n):
    if not isinstance(n, int):
        raise TypeError('the input is not an integer')
    if not n >= 0:
        raise ValueError('the expected input is a non-negative integer')

    lst = [0, 1]
    if not n > 1:
        return lst[n]
    for _ in range(n-1):
        lst.append(lst[-1] + lst[-2])
    return lst[n]

n = int(input())
print(calc_fib(n))
