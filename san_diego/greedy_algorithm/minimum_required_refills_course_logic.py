def minimum_refills(x, n, L):
    num_refills = 0
    current_refill = 0

    while current_refill <= n:
        last_refill = current_refill
        while (current_refill <= n) and ((x[current_refill+1] - x[last_refill]) <= L):
            current_refill += 1
        if current_refill == last_refill:
            return "IMPOSSIBLE"
        if current_refill <= n:
            num_refills += 1
    return num_refills


x = [0, 50, 420, 712, 888, 888, 1112, 1500, 1900, 2300]
n = len(x) - 2
L = 400

minimum_refills(x, n, L)