import random
from timeit import timeit

def get_greatest_common_divisor_slow(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('at least one of the inputs is not an integer')
    if a < 0 or b < 0:
        raise ValueError('both the inputs should be at least zero or more')

    if b > a: a, b = b, a

    if b == 0: return 0

    if a % b == 0: return b

    dict1 = {}
    for n in [a, b]:
        ls = []
        for d in range(1, b + 1):
            if n % d == 0:
                ls.append(d)
        dict1[n] = ls

    return max(set(dict1[a]).intersection(set(dict1[b])))


# this algorithm is known as the euclidean algorithm # key Lemma
def get_greatest_common_divisor_fast(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('at least one of the inputs is not an integer')
    if a < 0 or b < 0:
        raise ValueError('both the inputs should be at least zero or more')

    if b > a: a, b = b, a

    if b == 0: return a

    return get_greatest_common_divisor_fast(b, a % b)


if __name__ == '__main__':
    for _ in range(100):
        a, b = random.choices(range(10000000000000), k=2)
        assert get_greatest_common_divisor_fast(a, b) == get_greatest_common_divisor_fast(a, b), 'greatest common divisor implementation is wrong'
    mysetup1 = "from __main__ import get_greatest_common_divisor_slow"
    mystmt1 = "get_greatest_common_divisor_slow(3918848, 1653264)"
    mysetup2 = "from __main__ import get_greatest_common_divisor_fast"
    mystmt2 = "get_greatest_common_divisor_fast(3918848, 1653264)"
    t_1 = timeit(stmt=mystmt1, setup=mysetup1, number=1000)
    t_2 = timeit(stmt=mystmt2, setup=mysetup2, number=1000)
    print(f'greatest common factor - the time taken by looping method: {t_1}, the time taken by recursion method: {t_2}')

