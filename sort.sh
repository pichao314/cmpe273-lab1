#!/bin/bash
rm output/*.*
rm tmp/*.*
echo -e "Time of synchronized merge sort:\n" >time.txt
{ time ./ext_merge_sort.py; } 2>&1 | cat >>time.txt
rm output/*.*
rm tmp/*.*
echo -e "Time of asynchronized merge sort:\n" >async_time.txt
{ time ./async_ext_merge_sort.py; } 2>&1 | cat >>async_time.txt