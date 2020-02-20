#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    game = ['rock', 'paper', 'scissors']
    combinations = []

    def build_combination(rounds_left, result):
        if rounds_left == 0:
            combinations.append(result)
            return
        for el in game:
            build_combination(rounds_left - 1, result + [el])

    build_combination(n, [])
    return combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

print(rock_paper_scissors(2))
