#!/bin/bash
echo -e "Time of synchronized merge sort:\n" >time.txt
{ time ./ext_merge_sort.py ${file}; } 2>&1 | cat >>time.txt


for file in "input"/*; do
    echo -e "\nThe time of $file is" >>time.txt
done
