#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 20
100 200 125
201 210 89
900 1000 174



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
