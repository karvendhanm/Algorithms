# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):
    lst = [0, 1]
    if not n > 1:
        return lst[n]
    for _ in range(n-1):
        lst.append((lst[0] + lst[1])%10)
        del lst[0]

    return lst[1]%10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_fast(n))
