#!/usr/bin/python

import sys
import math

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # start at max number of cookies that it can eat (3) in the minimum amount of times i.e. for n = 9 it will be 3,3,3
    # then reduce the number of cookies sequentially by adding more eating times if needed to reach n i.e. n = 9 3,2,3,1 or 2,3,3,1
    # add each combination as a list inside the list as we go.
    # return number of items in the list
    if n == 2:
        return 2
    elif n < 2:
        return 1
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

# print(eating_cookies(5))
