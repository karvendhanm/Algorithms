# recursive algorithm to sort two arrays
import warnings
warnings.filterwarnings('ignore')

from basic_finctions import *
import time

lower_bound = int(input('Lower bound of the array to be sorted'))
upper_bound = int(input('Upper bound of the array to be sorted'))
size = int(input('size of the array to be sorted'))

lst = gen_int_array(lower_bound, upper_bound, size)

start = time.clock()
machine_sort = sorted(lst)
end = time.clock()
print('the time taken by the machine is {}'.format(end-start))


def sort_list(lst):
    '''

    :param lst:
    :return:
    '''

    status = True
    while (status):
        count = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                tmp = lst.pop(i)
                lst.insert(i + 1, tmp)
                count += 1
        if count == 0:
            status = False

    return lst


def combine_2_sorted_arrays(lst1, lst2):
    '''

    :param lst1:
    :param lst2:
    :return:
    '''

    # if lst1[0] > lst2[0]:
    #     lst1, lst2 = lst2, lst1
    #
    # for idx_2 in range(len(lst2)):
    #     for idx_1 in range(len(lst1)):
    #         try:
    #             if (lst2[idx_2] >= lst1[idx_1]) & (lst2[idx_2] <= lst1[idx_1+1]):
    #                 lst1.insert(idx_1+1, lst2[idx_2])
    #                 break
    #         except:
    #             lst1.insert(len(lst1), lst2[idx_2])
    #             break
    # return lst1

    i, j = 0, 0

    t = len(lst1) + len(lst2)
    final_lst = np.zeros(t)

    for k in range(t):
        try:
            if lst1[i] < lst2[j]:
                final_lst[k] = lst1[i]
                i += 1
            else:
                final_lst[k] = lst2[j]
                j += 1
        except:

            if i < len(lst1):
                final_lst[k:] = lst1[i:]
            elif j < len(lst2):
                final_lst[k:] = lst2[j:]
            break

    return final_lst


def merge_sort(lst):
    '''

    :param lst:
    :return:
    '''

    lst_len = len(lst)

    if lst_len <= 1:
        return lst
    elif lst_len == 2:
        return sort_list(lst)
    else:
        lst_split_len = lst_len // 2
        first_lst = lst[:lst_split_len]
        second_lst = lst[lst_split_len:]
        lst_final = combine_2_sorted_arrays(merge_sort(first_lst), merge_sort(second_lst))

    return lst_final

start = time.clock()
merge_sort = merge_sort(lst)
end = time.clock()
print('the time taken by merge sort is {}'.format(end-start))

if (machine_sort == merge_sort).all():
    print('The merge sort algorithm implementation is right')
else:
    print('The merge sort algorithm implementation still needs work')

## takes way too long to run
# start = time.clock()
# simple_sort = sort_list(lst)
# end = time.clock()
# print('the time taken by simple sort is {}'.format(end-start))




















