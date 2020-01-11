# Uses python3
import sys

def lcm_fast(a, b):
    if b > a: a, b = b, a

    if b == 0:
        return b
    elif a%b == 0:
        return a

    x = 2
    while True:
        if (a * x) % b == 0: return a*x
        x += 1



def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))


