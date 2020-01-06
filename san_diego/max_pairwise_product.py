# python3
import random

def find_max_num(numbers):

    if len(numbers) == 0:
        raise ValueError('the input argument must have atleast one numeral')

    max_num = numbers[0]
    for val in numbers[1:]:
        if val > max_num: max_num = val

    return max_num

def max_pairwise_product_fast(numbers):
    # lst = sorted(numbers, reverse=True)
    # return lst[0] * lst[1]
    if len(numbers) < 2:
        return 0

    max_num_1 = find_max_num(numbers)
    numbers.pop(numbers.index(max_num_1))
    max_num_2 = find_max_num(numbers)
    return max_num_1*max_num_2


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))







