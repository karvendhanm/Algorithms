'''
Compute F_n

Input: An integer n >= 0
Output: F_n

Fibonacci series - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''
from functools import lru_cache
from timeit import timeit

@lru_cache(maxsize = None)
def get_nth_fibonacci_number(n):
    if not isinstance(n, int):
        raise TypeError('the input is not an integer')
    if not n >= 0:
        raise ValueError('the expected input is a non-negative integer')

    if n <= 1:
        return n
    else:
        return get_nth_fibonacci_number(n-1) + get_nth_fibonacci_number(n-2)


fibonacci_cache = {}
def get_nth_fibonacci_number_own_cache(n):
    if not isinstance(n, int):
        raise TypeError('the input is not an integer')
    if not n >= 0:
        raise ValueError('the expected input is a non-negative integer')

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n <= 1:
        val = n
    else:
        val = get_nth_fibonacci_number_own_cache(n-1) + get_nth_fibonacci_number_own_cache(n-2)

    fibonacci_cache[n] = val
    return val



def get_nth_fibonacci_number_slow(n):
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


if __name__ == '__main__':
    for n in range(2000):
        # print(f'getting the nth fibonacci number: {n}')
        assert get_nth_fibonacci_number(n) == get_nth_fibonacci_number_slow(n), 'fibonacci implementation is wrong'
        assert get_nth_fibonacci_number(n) == get_nth_fibonacci_number_own_cache(n), 'fibonacci implementation is wrong'
        assert get_nth_fibonacci_number_slow(n) == get_nth_fibonacci_number_own_cache(n), 'fibonacci implementation is wrong'

    mysetup_1 = "from functools import lru_cache; from __main__ import get_nth_fibonacci_number"
    mystmt_1= "get_nth_fibonacci_number(100)"
    mysetup_2 = "from __main__ import get_nth_fibonacci_number_slow"
    mystmt_2= "get_nth_fibonacci_number_slow(100)"
    mysetup_3 = "from __main__ import get_nth_fibonacci_number_own_cache"
    mystmt_3 = "get_nth_fibonacci_number_own_cache(100)"
    t_1 = timeit(stmt=mystmt_1, setup=mysetup_1, number=1000000)
    t_2 = timeit(stmt=mystmt_2, setup=mysetup_2, number=1000000)
    t_3 = timeit(stmt=mystmt_3, setup=mysetup_3, number=1000000)
    print(f'Fibonacci - the time taken by recursion method: {t_1}, the time taken by loopin method: {t_2}')
    print(f'Fibonacci - the time taken by recursion method: {t_1}, the time taken by loopin method: {t_3}')
