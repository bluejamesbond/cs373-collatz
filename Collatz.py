#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]


# ------------
# collatz_eval
# ------------
cache = {}


def collatz_cycle_length(i):
    if i == 1:
        return 1
    if i in cache:
        return cache[i]

    if i % 2 == 0:
        i /= 2
    else:
        i = 3 * i + 1

    cycles = collatz_cycle_length(i)

    if i not in cache:
        cache[i] = cycles

    return 1 + cycles


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    assert 0 < i < 1000000
    assert 0 < j < 1000000

    max_cycles = 1

    if j < i:
        temp = i  # swap j and i
        i = j
        j = temp

    m = round(j / 2) + 1

    if i < m < j:
        i = m

    for curr in range(i, j + 1):
        cycles = collatz_cycle_length(curr)

        if cycles > max_cycles:
            max_cycles = cycles

    return max_cycles


# -------------
# collatz_print
# -------------

def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")


# -------------
# collatz_solve
# -------------

def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
