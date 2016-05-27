#!/usr/bin/env python2

import sys


def huge_fibonacci(n, m):
    if n > m:
        p = pisano_period_len(m)
        ans = fibonacci(n % p) % m
        return ans
    else:
        return fibonacci(n) % m


def pisano_period_len(m):
    if m < 2:
        raise Exception("pisano period requires m >= 2")

    i = 2
    j = 0
    k = 1

    while True:
        p = j + k
        j, k = k, p
        if p % m == 0 and (j + k) % m == 1:
            return i
        i += 1


def fibonacci(n):
    if n in (0, 1):
        return n

    i = 2
    j, k = 0, 1

    while i < n + 1:
        j, k = k, j + k
        i += 1

    return k


if __name__ == '__main__':
    n, m = [int(_) for _ in sys.stdin.readline().split()]
    print huge_fibonacci(n, m)
