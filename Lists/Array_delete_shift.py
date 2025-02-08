# Array Delete And Shift
'''
You are given an array arr(0-based indexing). The size of the array is given by n. You need to delete an element at given index and modify given 
array. The arr[i] of array is initially set to i+1. Deletion means you need to shift all the elements after that index to the left by 
1 position and set the last element as zero.

Example 1:
Input: n = 5
       index = 0
Output: 2 3 4 5 0
Your Task:
You don't need to read the input or print anything, as that is handled by the driver code. 
You only need to complete the function deleteFromArray() that takes arr, n, index as parameters and modifies the array arr as per requirements. 
'''
def deleteFromArray(arr,n,idx):
    #code here
    if 0 <= idx < n:
        for i in range(idx, n-1):
            arr[i] = arr[i+1]
        arr[n-1] = 0

