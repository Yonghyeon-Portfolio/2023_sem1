#!/bin/bash

for in_f in test/*.in; do
    out_f="${in_f%.*}.out"
    if ! [ -f "$out_f" ]; then
        echo -e "\033[31mMissing output file for ${in_f}\033[0m"
        continue
    fi
    # echo "Testing ${in_f}..."
    result=$(./greet < "$in_f" | diff - "$out_f")
    if [ "${#result}" -gt 0 ] 
    then
        echo -e "\033[31mTest failed for ${in_f}\033[0m"
        echo ${result}
    else
        echo -e "\033[32mTest passed for ${in_f}\033[0m"
    fi
done
