# A recursive algorithm to multiply two numbers

from ast import literal_eval
# from basic_finctions import *


x = float(input('Enter the first number (only float or an integer is allowed)'))
y = float(input('Enter the second number (only float or an integer is allowed)'))

def count_number_of_digits(num):
    '''

    :param num: An integer
    :return: The number of digits in the integer
    '''

    if (isinstance(num, int)) | (isinstance(num, float)):
        num = abs(int(num))

        # if the given number is zero itself, then it has 1 digit
        if num == 0:
            return 1

        count = 0

        while num > 0:
            num = num // 10
            count += 1
        return count
    else:
        print(f'the given input {num} must be a number')

def gaussian_trick(a, b, c, d):
    '''

    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    '''

    return (multiply_two_numbers(a, c) + multiply_two_numbers(a, d) + multiply_two_numbers(b, c) + multiply_two_numbers(b, d))


def multiply(a, b, c, d, n):
    '''

    :param a:
    :param b:
    :param c:
    :param d:
    :param n1:
    :param n2:
    :return:
    '''

    a_c = multiply_two_numbers(a, c)
    b_d = multiply_two_numbers(b, d)

    num = gaussian_trick(a, b, c, d)

    prod = (a_c *literal_eval('1e'+str(literal_eval(str(2*n))))) + \
           ((num - (a_c + b_d)) * literal_eval('1e'+str(literal_eval(str(n))))) + b_d

    return prod



def multiply_two_numbers(x_1, x_2):
    '''

    :param x_1: First number to be multiplied
    :param x_2: Second number to be multiplied
    :return: Product of the first and the second number
    '''

    num_digits_1 = count_number_of_digits(x_1)
    num_digits_2 = count_number_of_digits(x_2)

    if (num_digits_1 == 1) & (num_digits_2 == 1):
        return x_1 * x_2
    elif (num_digits_1 > 1) & (num_digits_2 > 1):
        n = num_digits_2 // 2
        if num_digits_1 <= num_digits_2:
            n = num_digits_1 // 2

        denominator_1 = literal_eval('1e'+str(literal_eval(str(n))))
        denominator_2 = literal_eval('1e'+str(literal_eval(str(n))))

        a = x_1 // denominator_1
        b = x_1 % denominator_1
        c = x_2 // denominator_2
        d = x_2 % denominator_2

        prod = multiply(a, b, c, d, n)
    else:
        if num_digits_1 == 1:
            a = 0
            b = x_1

            n = num_digits_2 // 2
            denominator = literal_eval('1e' + str(literal_eval(str(n))))

            c = x_2 // denominator
            d = x_2 % denominator

            prod = multiply(a, b, c, d, n)
        else:
            c = 0
            d = x_2

            n = num_digits_1 // 2
            denominator = literal_eval('1e' + str(literal_eval(str(n))))

            a = x_1 // denominator
            b = x_1 % denominator

            prod = multiply(a, b, c, d, n)

    return prod


recursive_mul = multiply_two_numbers(x, y)
machine_mul =  x * y

if recursive_mul == machine_mul:
    print('Recursive multiplication implementation is correct')

print('the local algo answer is {:.2f}\nthe mchne algo answer is {:.2f}'.format(recursive_mul, machine_mul))
