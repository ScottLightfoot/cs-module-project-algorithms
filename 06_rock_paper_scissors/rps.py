#!/usr/bin/python

import sys

outcomes = ['rock'], ['paper'], ['scissors']

def add_layer(curr_list):
    return [i + j for i in curr_list for j in outcomes]

def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    else:
        # cartesian product?
        ret_list = [i for i in outcomes]
        while n > 1:
            ret_list = add_layer(ret_list)
            n -= 1
        return ret_list

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
