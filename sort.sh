#!/bin/bash
rm output/sorted.txt
echo -e "Time of synchronized merge sort:\n" >output/time.txt
{ time ./ext_merge_sort.py; } 2>&1 | cat >>output/time.txt
rm output/async_sorted.txt
echo -e "Time of asynchronized merge sort:\n" >output/async_time.txt
{ time ./async_ext_merge_sort.py; } 2>&1 | cat >>output/async_time.txt
