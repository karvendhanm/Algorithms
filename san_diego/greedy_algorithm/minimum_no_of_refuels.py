# This problem seeks to find the minimum number of refueling stops to get from point A to point B
# seperated by distance(L) in km. There are number of gas stations in between A and B whose
# distances from A is given by the list x in kms. Also, the maximum distance that a car could
# travel after one refueling is given by n in kms.

import numpy as np

def minimum_required_refills(x, n, L):
    if len(x) > 0:
        while max(x) > L:
            x.remove(max(x))

    x_arr = np.array(sorted(x))
    bool_arr = x_arr <= n
    if sum(bool_arr) == 0:
        return np.nan

    dist_travelled = x_arr[bool_arr][-1]
    if (dist_travelled + n) >= L:
        return 1

    return 1 + minimum_required_refills(list(x_arr[np.logical_not(bool_arr)] - dist_travelled), n, L-dist_travelled)


x = [0, 50, 420, 712, 888, 888, 1112, 1500, 1900]
n = 400
L = 2301

print(minimum_required_refills(x, n, L))


