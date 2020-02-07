# Uses python3
import sys

def get_change(m):
    #write your code here

    count = 0
    for denom in [10, 5, 1]:
        num_coins = m//denom
        if num_coins:
            count += num_coins
            m -= (num_coins * denom)
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
