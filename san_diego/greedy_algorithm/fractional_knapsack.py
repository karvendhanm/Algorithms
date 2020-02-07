# Uses python3
import sys
import numpy as np
from operator import itemgetter

def get_optimal_value(capacity, weights, values):
    # write your code here
    value = 0.0
    weights = np.array(weights)
    values = np.array(values)

    unit_val = values / weights
    s_order = unit_val.argsort()[::-1]
    unit_val = unit_val[s_order]
    weights = weights[s_order]

    for idx, w in enumerate(weights):

        if capacity == 0:
            return value

        m = min(capacity, w)
        value = value + (m * unit_val[idx])

        capacity -= m
        w -= m

    return value
    
    
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
