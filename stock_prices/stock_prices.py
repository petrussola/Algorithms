#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # selling can only take place after buying
    # so we need to check the profit between X number and Y number (Y being after X in the list)
    # we don't need to loop over the last item because we need 2 operations, buy and sell
    # if we only get one item in the array, we should return error message because we need at least two prices
    # for each price, we check the rest of the items in the array
    # we keep track of biggest difference in a variable
    # this variable needs to be defined before the start of the loop and gets updated we encounter a new high
    # we'll start with iteration as first pass, and try recursion on the second
    # if 2nd price examined is lower, we will ignore because we need to sell at a gain
    if len(prices) < 2:
        return "Sorry buddy, need two prices in order to buy and sell."
    biggest_difference_so_far = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] != prices[i] and (prices[j] - prices[i]) > biggest_difference_so_far:
                biggest_difference_so_far.append = prices[j] - prices[i]
    return max(biggest_difference_so_far)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

test = [10, 7, 5, 8, 11, 9]
print(find_max_profit(test))