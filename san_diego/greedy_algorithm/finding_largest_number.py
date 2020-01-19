from itertools import permutations
from operator import itemgetter
import random
import timeit

# this method uses pythons inbuilt methods
def get_largest_number_inbuilt(lst):
    '''
    concatenates the biggest number out of the numbers in the lst.
    input will always be non-negative integers
    example:
    input: [569, 581, 57, 517, 52, 532, 5]
    output: 58157569553252517
    :param lst:
    :return:
    '''

    _lst = []
    for tup in permutations(lst, len(lst)):
        _lst.append(int("".join([str(val) for val in tup])))
    return max(_lst)

# Extremely slow method for accomplishing the task
def get_largest_number_slow(lst):
    '''
        concatenates the biggest number out of the numbers in the lst.
        input will always be non-negative integers
        example:
        input: [569, 581, 57, 517, 52, 532, 5]
        output: 58157569553252517
        :param lst:
        :return:
        '''

    change = 1
    while change:
        change = 0
        for idx, val in enumerate(lst[:-1]):
            if int(str(val) + str(lst[idx+1])) < int(str(lst[idx+1]) + str(val)):
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                change = 1

    return int("".join([str(val) for val in lst]))


def get_largest_number_relatively_fast(lst):
    l_o_lst = [(x, list(str(x))) for x in lst]
    max_len = max([len(value) for key, value in l_o_lst])
    for _, val in l_o_lst:
        while len(val) < max_len:
            val.insert(len(val), val[0])
    l_o_lst = [(key, int("".join(val))) for key, val in l_o_lst]
    l_o_lst = sorted(l_o_lst, key=itemgetter(1), reverse=True)
    return int("".join([str(key) for key, _ in l_o_lst]))


if __name__ == "__main__":
    for _ in range(10):
        lst = random.choices(range(10000), k=random.choice(range(1, 100)))
        assert get_largest_number_relatively_fast(lst) == get_largest_number_inbuilt(lst), 'greedy algorithm implementation is wrong'
    mystmt = '''get_largest_number_relatively_fast([5, 52, 57, 517, 532, 569, 581])'''
    mysetup = '''from operator import itemgetter; from __main__ import  get_largest_number_relatively_fast'''
    t_mymethod = timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000)
    builtinstmt = '''get_largest_number_inbuilt([5, 52, 57, 517, 532, 569, 581])'''
    builtinsetup = '''from itertools import permutations; from __main__ import  get_largest_number_inbuilt'''
    t_builtin = timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000)
    print(f'time taken my method is: {t_mymethod}')
    print(f'time taken builtin method is: {t_builtin}')



