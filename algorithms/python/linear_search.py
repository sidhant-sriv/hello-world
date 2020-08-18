#This is linear search in python
#Simple scan of the list
from random import randint
def linear_search(arr,x):
    i = 0
    while i<len(arr):
        if arr[i]==x:
            break
        else:
            i += 1
    if i>=len(arr):
        return -1
    return i
#Driver code
arr = [randint(1,100) for i in range(20)]
print(arr,linear_search(arr,20))