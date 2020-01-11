# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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


def find_last_digit(lst, n):
    l = len(lst)
    s = sum(lst)
    q = n // l
    r = n % l
    return ((s * q) + sum(lst[:r + 1]))


def fibonacci_partial_sum_fast(m, n):
    lst = find_fibonacci_modulo_pattern()
    n_ = find_last_digit(lst, n)
    m_ = find_last_digit(lst, m-1)
    return (n_-m_)%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))