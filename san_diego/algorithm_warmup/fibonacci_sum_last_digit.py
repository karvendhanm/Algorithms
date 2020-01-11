# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

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
        lst.append(get_nth_fibonacci_number_own_cache(i)%10)
        if len(lst)%2 == 0:
            x = len(lst)//2
            if lst[:x] == lst[x:]:
                return lst[:x]
        i+=1


def get_fibonacci_sum_last_digit_fast(n):
    lst = find_fibonacci_modulo_pattern()
    l = len(lst)
    s = sum(lst)
    q = n // l
    r = n % l
    return ((s*q)+sum(lst[:r+1]))%10


get_fibonacci_sum_last_digit_fast(3)
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(get_fibonacci_sum_last_digit_fast(n))
