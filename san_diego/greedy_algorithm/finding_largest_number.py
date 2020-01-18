from itertools import permutations
import random

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

def get_largest_number(lst):
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



if __name__ == "__main__":
    for _ in range(100):
        lst = random.choices(range(100000), k=random.choice(range(100)))
        assert get_largest_number(lst) == get_largest_number_inbuilt(lst), 'greedy algorithm implementation is wrong'






