#!/bin/bash

rm -rf collatz-tests

git clone https://github.com/cs373-fall-2015/collatz-tests/

echo "" > RunCollatz.log
echo "----- Running Tests -----"
echo ""

i=0
e=0

for f in collatz-tests/*.in
do
    i=$((i+1))
    out=${f/.in/.out}
    echo "Running $f"
    echo "Test #$i: $f" >> RunCollatz.log
    T="$(date +%s)"
    res=$(./RunCollatz.py < ${f} > RunCollatz.tmp 2>&1)
    T="$(($(date +%s)-T))"
    echo "Runtime: $T seconds"  >> RunCollatz.log
    if [ -n "$res" ]
    then
    echo "Output: $res" >> RunCollatz.log
    fi
    diff --brief RunCollatz.tmp "$out"
    if [ "$?" != "0" ]
    then
    diff RunCollatz.tmp "$out" >> RunCollatz.log
    e=$((e+1))
    else
    echo "No problems"
    fi

    echo "Runtime: $T seconds"
    echo ""

    echo "----------" >> RunCollatz.log
    echo "" >> RunCollatz.log
    echo "" >> RunCollatz.log
done

echo "Total Tests: $i" >> RunCollatz.log
echo "Failed Tests: $e" >> RunCollatz.log

rm -rf collatz-tests