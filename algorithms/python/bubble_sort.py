#This is code for bubble sort.
from utils import utils
def bubble(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
                if(arr[i]>arr[i+1]):
                    utils.swap_in_arr(arr,i,i+1)
                else: pass
    return arr
        
#Driver code
x = [5,2,6,7,3,8,1,9,4,0]
print(bubble(x))