#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random
import time

# Function for searching un-ordered list to check if an item exists in the list. 
# Also returns the length of time the search required.
def sequential_search(a_list, item):
    start_time = time.time()
    position = 0
    found = False

    while position < len(a_list) and not found:
        if a_list[position] == item:
            found = True
        else:
            position = position + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)

# Function for searching ordered list to check if an item exists in the list.
# Also returns the length of time the search required.
def ordered_sequential_search(a_list, item):
    a_list = sorted(a_list)

    start_time = time.time()
    position = 0
    found = False
    end = False

    while position < len(a_list) and not found and not end:
        if a_list[position] == item:
            found = True
        else:
            if a_list[position] > item:
                end = True
            else:
                position = position + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)

# Function for searching ordered list to check if an item exists in the list using binary iterative method.
# Also returns the length of time the search required.
def binary_search_iterative(a_list, item):
    a_list = sorted(a_list)

    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)

# Function for searching ordered list to check if an item exists in the list using binary recursive method.
# Also returns the length of time the search required.
def binary_search_recursive(a_list, item):
    a_list = sorted(a_list)

    start_time = time.time()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)

# Function to generate list of random values
def list_gen(value):
    random_list = random.sample(range(1, (value + 1)), value)
    return random_list

# Main function for displaying how long each search function takes on average
def main():
    list_size = [500, 1000, 10000]
    search = {'Sequential': 0, 'Ordered': 0, 'Binary Iterative': 0, 'Binary Recursive': 0}

    for t_list in list_size:
        counter = 0
        while counter < 100:
            list_test = list_gen(t_list)
            search['Sequential'] += sequential_search(list_test, -1)[0]
            search['Ordered'] += ordered_sequential_search(list_test, -1)[0]
            search['Binary Iterative'] += binary_search_iterative(list_test, -1)[0]
            search['Binary Recursive'] += binary_search_recursive(list_test, -1)[0]
            counter += 1

        print ('For the list containing %s lines:' % (t_list))

        for st in search:
            print ('%s Search took %10.7f seconds to run, on average.' % (st, search[st] / counter))


if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




