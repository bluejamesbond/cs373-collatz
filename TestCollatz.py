#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve


# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "-5 100000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, -5)
        self.assertEqual(j, 100000000)

    def test_read_3(self):
        s = "6 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 6)
        self.assertEqual(j, 0)

    def test_read_4(self):
        s = "100000000 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100000000)
        self.assertEqual(j, 0)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 12, 0, 20000000000000)
        self.assertEqual(w.getvalue(), "12 0 20000000000000\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 0, '', 0)
        self.assertEqual(w.getvalue(), "0  0\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, '', '', '')
        self.assertEqual(w.getvalue(), "  \n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self):
        r = StringIO("1 1\n100 100\n210 210\n999999 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n100 100 26\n210 210 40\n999999 999999 259\n")

    def test_solve_2(self):
        r = StringIO("1000 1000\n1000 1001\n4000 40001\n2 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1000 1000 112\n1000 1001 143\n4000 40001 324\n2 1 2\n")

    def test_solve_3(self):
        r = StringIO("999999 999999\n900000 900000\n900001 900002\n9000 8999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "999999 999999 259\n900000 900000 158\n900001 900002 189\n9000 8999 185\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
