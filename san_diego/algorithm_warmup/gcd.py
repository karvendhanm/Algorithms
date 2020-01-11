# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def get_greatest_common_divisor_fast(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('at least one of the inputs is not an integer')
    if a < 0 or b < 0:
        raise ValueError('both the inputs should be at least zero or more')

    if b > a: a, b = b, a

    if b == 0: return a

    return get_greatest_common_divisor_fast(b, a % b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(get_greatest_common_divisor_fast(a, b))
