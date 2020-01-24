import numpy as np
from operator import itemgetter

def unit_cost_func(l1, l2):
    lst = [0 for _ in range(len(l2))]
    for idx, val in enumerate(l1):
        if val != 0:
            lst[idx] = l2[idx]/val
    return lst

def knapsack(knapsack_capacity, items_quantity, items_total_cost):
    possible_max_val = 0
    num_items = len(items_quantity)
    each_item_Amount_taken = [0 for _ in range(len(items_quantity))]

    item_unit_price = unit_cost_func(items_quantity, items_total_cost)

    for _ in range(num_items):

        if knapsack_capacity == 0:
            return (possible_max_val, each_item_Amount_taken)

        idx = item_unit_price.index(max(item_unit_price))
        q = min(items_quantity[idx], knapsack_capacity)

        knapsack_capacity -= q
        items_quantity[idx] -= q
        each_item_Amount_taken[idx] = each_item_Amount_taken[idx]+q
        possible_max_val = possible_max_val + (q * item_unit_price[idx])

        if items_quantity[idx] == 0: item_unit_price[idx] = 0

    return possible_max_val, each_item_Amount_taken



knapsack(22, [4, 8, 35], [60, 40, 1])








