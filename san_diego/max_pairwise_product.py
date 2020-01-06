# python3
import random

def find_max_num(numbers):
    if len(numbers) == 0:
        return 0

    max_num = numbers[0]
    for val in numbers[1:]:
        if val > max_num: max_num = val

    return max_num

def max_pairwise_product_fast(numbers):
    # lst = sorted(numbers, reverse=True)
    # return lst[0] * lst[1]
    if len(numbers) == 0:
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

    # random.seed(124)
    # n = random.randint(0, 10)
    # input_numbers = random.choices(range(0, 10000), k=n)

    # stress test module is written below and commented out.
    # random.seed(123)
    # while True:
    #     n = random.randint(0, 10000)
    #     input_numbers = random.choices(range(0, 10000), k=n)
    #     # print('given_solution', max_pairwise_product(input_numbers))
    #     # print('my_solution', max_pairwise_product_fast(input_numbers))
    #     print(f'the numbers are: {input_numbers}')
    #     print(f'the length of the list is: {n}')
    #     gn_soln = max_pairwise_product(input_numbers)
    #     my_soln = max_pairwise_product_fast(input_numbers)
    #     print(f'given solution is  {gn_soln} my solution is {my_soln}')
    #     if (gn_soln != my_soln):
    #         break
    #     print('OK, everything working fine')





