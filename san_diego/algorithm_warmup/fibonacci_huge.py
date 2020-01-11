# Uses python3
import sys
from functools import lru_cache

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


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


def find_fibonacci_modulo_pattern(m):
    i=0
    lst = []
    while True:
        lst.append(get_nth_fibonacci_number_own_cache(i)%m)
        if len(lst)%2 == 0:
            x = len(lst)//2
            if lst[:x] == lst[x:]:
                return lst[:x]
        i+=1


def get_fibonacci_huge_fast(n, m):
    lst = find_fibonacci_modulo_pattern(m)
    return lst[n%len(lst)]



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))

