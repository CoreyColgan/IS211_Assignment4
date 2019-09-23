#!/usr/bin/env python
# coding: utf-8

import time
import random

# Function that will sort a list and return the amount of time the sort takes
def insertion_sort(a_list):

    start_time = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end_time = time.time()
    run_time = end_time - start_time
    return (run_time, a_list)

# Function that will sort a list using gap insertion method
def gap_insertion_sort(a_list, start, gap):
    
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

# Function that will sort a list using shell sort method
def shell_sort(a_list):

    start_time = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    end_time = time.time()
    run_time = end_time - start_time
    return (run_time, a_list)

# Function that will sort a list using python sort method
def python_sort(a_list):
    
    start_time = time.time()
    a_list.sort()
    end_time = time.time()
    run_time = end_time - start_time
    return (run_time, a_list)

# Function to create a list of random values
def list_gen(value):

    sample_list = random.sample(range(1, (value + 1)), value)
    return sample_list

# Main function to test sort functions
def main():
    
    list_size = [500, 1000, 10000]
    sort = {'Insertion': 0, 'Shell': 0, 'Python': 0}

    for t_list in list_size:
        counter = 0
        while counter < 100:
            list_test = list_gen(t_list)
            sort['Insertion'] += insertion_sort(list_test)[0]
            sort['Shell'] += shell_sort(list_test)[0]
            sort['Python'] += python_sort(list_test)[0]
            counter += 1

        print ('For the list containing %s lines:' % (t_list))

        for st in sort:
            print ('The %s Search took %.5f seconds to run.' % (st, sort[st] / counter))

if __name__ == '__main__':
    main()
