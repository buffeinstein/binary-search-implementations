#!/bin/python3


def find_smallest_positive(xs):
    '''
    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if len(xs) == 0:
        return None

    left = 0
    right = len(xs) - 1

    while left != right:
        mid = (left + right) // 2
        if xs[mid] == 0:
            return mid + 1
        elif xs[mid] < 0:
            left = mid + 1
        elif xs[mid] > 0:
            if xs[mid - 1] <= 0:
                return mid
            right = mid

    if xs[left] > 0:
        return left
    else:
        return None


def count_repeats(xs, x):
    '''
    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    xs.reverse()

    def first(xs, x):
        left = 0
        right = len(xs) - 1

        while left != right:
            mid = (left + right) // 2
            if xs[mid] == x:
                if xs[mid - 1] < x:
                    return mid
                else:
                    right = mid
            if xs[mid] < x:
                left = mid + 1
            if xs[mid] > x:
                right = mid

        if xs[left] == x:
            return left
        else:
            return None

    def last(xs, x):
        left = 0
        right = len(xs) - 1

        while left != right:
            mid = (left + right) // 2
            if xs[mid] == x:
                if xs[mid + 1] > x:
                    return mid
                else:
                    left = mid + 1
            if xs[mid] < x:
                left = mid + 1
            if xs[mid] > x:
                right = mid

        if xs[left] == x:
            return left
        else:
            return None

    if len(xs) == 0:
        return 0

    if first(xs, x) is None:
        return 0

    else:
        return last(xs, x) - first(xs, x) + 1


def argmin(f, lo, hi, epsilon=1e-3):
    if hi - lo < epsilon:
        return (lo + hi) / 2

    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3

    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)

# the functions below are extra credit
#
# def find_boundaries(f):
#   # lo = 1
#   # hi = 1
#   # mid = (lo+hi)/2
#   # if f(lo) > f(mid):
#   #     lo = lo  * 2
#   #     find_boundaries(f(lo))
#   # elif (f(hi) < f(mid)):
#   #     hi = hi * 2
#   #     find_boundaries(f(hi))
#   # else:
#   #     a = (lo, hi)
#   #     return a
#
# def argmin_simple(f, epsilon=1e-3):
#    lo, hi = find_boundaries(f)
#    return argmin(f, lo, hi, epsilon)
