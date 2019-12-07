# A function must have two blank lines before it
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


def is_even(num):
    '''

    :param num: A number
    :return: The number is even or not
    '''
    if (isinstance(num, int)) | (isinstance(num, float)):
        if num % 2 == 0:
            return True
        else:
            return False
    else:
        print(f'the given input {num} must be a number')

# x = int(input('please enter a number(integer)'))
# y = int(input('please enter another number(integer)'))