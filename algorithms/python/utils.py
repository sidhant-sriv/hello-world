#utility functions that I am too lazy write over and over again. :P
import time
import random
#Function to swap array elements
def swap_in_arr(arr,index1,index2):
    arr[index1],arr[index2] = arr[index2],arr[index1]
#Function to give the time taken by the function.
def timing(func):
    t0 = time.perf_counter_ns()
    f = func
    t1 = time.perf_counter_ns() - t0
    return t1
def rand_arr(length,l = 0,r = 1_000):
    return [random.randint(l,r) for i in range(length+1)]