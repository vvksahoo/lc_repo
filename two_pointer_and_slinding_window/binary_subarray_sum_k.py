"""
930. Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

"""

def numSubarraysWithSum(nums, goal):
    left = 0
    num_subarray = 0
    count = 0
    
    while left < len(nums):
        right = left
        count = 0
        while right < len(nums):
            count = count + nums[right]
            if count == goal:
                num_subarray += 1
            elif count > goal:
                break
            right += 1
        left += 1
    
    return num_subarray

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums, goal))

def numSubarraysWithSumOptimized(nums, goal):
    """
    The count of subarrays with sum at most goal includes all subarrays with sum less than or equal to goal.
    The count of subarrays with sum at most goal - 1 includes all subarrays with sum strictly less than goal.
    Their difference gives exactly the number of subarrays with sum equal to goal.
    To efficiently count subarrays with sum at most a given value, a sliding window is used:

    Expand the window to the right, adding elements to the current sum.
    If the sum exceeds the target, shrink the window from the left until the sum is within the limit.
    For each position, the number of valid subarrays ending at the current right pointer is (right - left + 1).


    Time: O(n+n)
    Space: O(1)
    """
    left = 0
    num_subarray = 0
    count = 0
    right = 0
    
    while right < len(nums):
        count = count + nums[right]
        
        while count > goal:
            count = count - nums[left]
            left += 1
        if count <= goal:
            num_subarray  = num_subarray + (right - left + 1) # we are adding lenght here basically because let say, we have [1,0,0,1] at last index we can have 4 subarray which sum is 2

        right += 1
    
    return num_subarray

nums = [1,0,1,0,1]
goal = 2
number_subarray = (numSubarraysWithSumOptimized(nums, goal) - numSubarraysWithSumOptimized(nums, goal-1))
print(number_subarray)


