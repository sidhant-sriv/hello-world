#This is code for bubble sort.
import utils
import random

def bubble(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
                if(arr[i]>arr[i+1]):
                    utils.swap_in_arr(arr,i,i+1)
                else: pass
    return arr
        
