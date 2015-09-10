#!/usr/bin/env bash

echo "import sys" > _SphereCollatz.py
echo "" >> _SphereCollatz.py
paste Collatz.py >> _SphereCollatz.py
echo "" >> _SphereCollatz.py
echo "if __name__=='__main__':collatz_solve(sys.stdin,sys.stdout)" >> _SphereCollatz.py
pyminifier _SphereCollatz.py > SphereCollatz.py
python3 -m mnfy SphereCollatz.py > _SphereCollatz.py
paste _SphereCollatz.py > SphereCollatz.py
rm -rf _SphereCollatz.py