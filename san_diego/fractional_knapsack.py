import numpy as np
from operator import itemgetter

def unit_cost_func(l1, l2):
    lst = [0 for _ in range(len(l2))]
    for idx, val in enumerate(l2):
        if val != 0:
            lst[idx]=l1[idx]/val
    return lst

def knapsack(knapsack_capacity, items_quantity, items_cost):
    possible_max_val = 0
    num_items = len(items_quantity)
    each_item_Amount_taken = [0 for _ in range(len(items_quantity))]

    lst = []

    for n, p, d, q in zip(range(num_items), items_quantity, items_cost, unit_cost_func(items_quantity, items_cost)):
        lst.append((n, p, d, q))

    for idx in range(num_items):
        if knapsack_capacity == 0:
            return (possible_max_val, each_item_Amount_taken)

        lst.sort(key=itemgetter(3), reverse=True)

    return lst


knapsack(7, [4, 3, 2], [5, 4, 3])








