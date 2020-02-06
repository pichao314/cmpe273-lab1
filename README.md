# CMPE273-LAB1

## Introduce

### Environment

- OS
  - Ubuntu 18.04
  - MacOS 10.15.3
- Python 3.7.3
- Asyncio 3.4.3

### Instruction

Execute the `sort.sh` file to sort by sync and async version merge sort and output the result into `output/` folder as well.

```sh
sh sort.sh
```

## Result Compare

| time | Synchronous | Asynchronous |
| ---- | ----------- | ------------ |
| real | 0m0.143s    | 0m0.245s     |
| user | 0m0.110s    | 0m0.207      |
| sys  | 0m0.029     | 0m0.034      |

After comparing we can see that the the asynchronous version of external sort did not perform better, this may due to the size of data is not big enough, therefore the time delay of coroutine task switch may cost more then the time saved by async-sorting multiple input files.

## Algorithm Introduce

### External Sort

As for the limitation of RAM in external sort, there have multiple inbuffs for each input files that keep reading limited buck of data each time, and there have a outbuff that keep accepting the compared result from each inbuff and output to the sorted file once filled.

### Asynchronous

The asyncio module is used in the sorting or each single file. Without asyncio, the sorting of one file should be waited until the former file was sorted. With asyncio, all the sorting task can be placed in a event loop that the main task do not have to wait one by one.

>Inbuff used RAM: 9
>
>Inbuff count: 10
>
>Outbuff used RAM:10
>
>Outbuff count: 1
>
>Total Used RAM: 9 * 10 + 10 = 100

## Appendix(Requirements)

Use any kind of [External Sorting](https://en.wikipedia.org/wiki/External_sorting) algorithm to sort all numbers from input/unsorted_*.txt files and save the sorted result into output/sorted.txt file amd async_sorted.txt file.

Implement your solution with or without [Asyncio](https://docs.python.org/3/library/asyncio.html).

* ext_merge_sort.py
* async_ext_merge_sort.py (uses Asyncio)

Finally, measure each execution time via

```sh
time python3 ext_merge_sort.py
time python3 async_ext_merge_sort.py
```

Save the output of each run in time.txt and async_time.txt.

Commit your changes into your public Github repository (cmpe273-lab1) and your final commit should have:

1. ext_merge_sort.py
2. async_ext_merge_sort.py
3. all unsorted_*.txt files
4. all sorted_.txt files
5. time.txt and async_time.txt
