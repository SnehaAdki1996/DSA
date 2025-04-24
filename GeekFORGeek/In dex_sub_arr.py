# Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

# Note: If no such array is possible then, return [-1].

# Input: arr[] = [1, 2, 3, 7, 5], target = 12
# Output: [2, 4]
# Explanation: The sum of elements from 2nd to 4th position is 12.

def subarraySum(self, arr, target):
    # code here
    for i in range(0,len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum = sum+arr[j]
            if sum > target:
                break;
            elif sum == target:
                return[i+1,j+1]
                
    return [-1]


