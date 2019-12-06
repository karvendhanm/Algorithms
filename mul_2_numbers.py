# A recursive algorithm to multiply two numbers

def count_number_of_digits(num):
    '''

    :param num: An integer
    :return: The number of digits in the integer
    '''

    if (isinstance(num, int)) & (num > 0):
        count = 0
        while num > 0:
            num = num // 10
            count += 1
        return count
    else:
        print(f'the given input {num} is not a positive integer')


x = int(input('please enter a number(integer)'))
y = int(input('please enter another number(integer)'))

