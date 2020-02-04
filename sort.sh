#!/bin/bash
echo -e "Time of synchronized merge sort:\n" >time.txt
{ time ./ext_merge_sort.py; } 2>&1 | cat >>time.txt
