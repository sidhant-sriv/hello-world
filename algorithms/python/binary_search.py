#This is binary search in python.
#works best with sorted lists.
def binary_search(arr,l,r,x):
    mid  = (l+r)//2 
    if(l<=r):
        if(arr[mid] == x):
            return mid
        elif(arr[mid]>x):
            return binary_search(arr,l,mid-1,x)
        elif(arr[mid]<x):
            return binary_search(arr,mid+1,r,x)
    else:
        return -1
arr = [i for i in range(100)]
print(binary_search(arr,0,len(arr)-1,4))

    