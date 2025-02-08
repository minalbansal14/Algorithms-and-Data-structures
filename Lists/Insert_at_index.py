'''
You are given an array arr(0-based index). The size of the array is given by sizeOfArray. You need to insert an element at given index.
Example 1:
Input: sizeOfArray = 6
       arr[] = {1, 2, 3, 4, 5}
       index = 5, element = 90
Output: 1 2 3 4 5 90

Explanation: 90 is inserted at index
             5(0-based indexing). After inserting,
array elements are like: 1, 2, 3, 4, 5, 90.

Your Task: You don't need to read input or print anything.. The input is already taken care of by the driver code. 
You only need to complete the function insertAtIndex() that takes arr, sizeOfArray, index, element as input and modifies the array arr as per requirements. 
The printing is done by driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''
def insertAtIndex(arr, sizeOfArray, index, element):
      return arr.insert(index, element)
