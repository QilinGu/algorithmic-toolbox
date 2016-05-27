#!/usr/bin/env python2

import sys


def fibonacci_last_digit(n):
    if n in (0, 1):
        return n

    i = 2
    j, k = 0, 1

    while i < n + 1:
        j, k = k, j + k
        i += 1

    return k % 10


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(fibonacci_last_digit(n))