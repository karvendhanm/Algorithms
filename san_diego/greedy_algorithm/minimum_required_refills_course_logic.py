# We need to go from point A to point B.
# There are n gas stations in between A and B.
# x - array of distance of gas stations from point A. note: both starting point(A, 0kms) and the destination(B) have also been included in the array x.
# n - number of gas stations in between A and B
# L - number of kilometers that can be travelled in single refueling.

def minimum_refills(x, n, L):
    num_refills, current_refill = 0, 0

    while current_refill <= n:
        last_refill = current_refill
        while (current_refill <= n) and ((x[current_refill+1] - x[last_refill]) <= L):
            current_refill += 1
        if last_refill == current_refill:
            return "IMPOSSIBLE"
        if current_refill <= n:
            num_refills += 1
    return num_refills

x = [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200] # dista
n = len(x) - 2
L = 400

minimum_refills(x, n, L)