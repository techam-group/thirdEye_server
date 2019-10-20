import json
import numpy as np
import sys


# Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    print(lines)
    return json.load(lines[0])


def main():
    # get our data as an array from read_in()
    lines = read_in()

    # create a numpy array
    np_lines = np.array(lines)
    print(np_lines)

    # use numpy's sum method to find sum of all elements in the array
    lines_sum = np.sum(np_lines)

    # return the sum to the output stream
    print(lines_sum)


# start process
if __name__ == '__main__':
    main()
