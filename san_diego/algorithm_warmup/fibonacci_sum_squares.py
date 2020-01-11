# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

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


def find_fibonacci_modulo_pattern():
    i=0
    lst = []
    while True:
        lst.append((get_nth_fibonacci_number_own_cache(i)**2)%10)
        if len(lst)%2 == 0:
            x = len(lst)//2
            if lst[:x] == lst[x:]:
                return lst[:x]
        i+=1


def fibonacci_sum_squares_fast(n):
    lst = find_fibonacci_modulo_pattern()
    l = len(lst)
    s = sum(lst)
    q = n // l
    r = n % l
    return ((s*q)+sum(lst[:r+1]))%10

# fibonacci_sum_squares_fast(1234567890)
if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
