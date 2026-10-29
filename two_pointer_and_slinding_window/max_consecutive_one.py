"""
485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

def findMaxConsecutiveOnes(nums):
    """
    Brute force, O(n^2), O(1), calculate all possible subarrays and find the max length
    """
    left = 0
    maxLen = 0
    while left < len(nums):
        right = left
        while right < len(nums):
            if nums[right] == 0: break
            maxLen = max(maxLen, (right-left+1))
            right += 1
        left += 1
    return maxLen

nums = [1,1,0,0, 1, 0,1,1,1, 0, 1,1,1,1]
print(findMaxConsecutiveOnes(nums))

def findMaxConsecutiveOnes(nums):
    left = 0
    maxLen = 0
    right = 0
    while right < len(nums):
        if  nums[right] == 0:
            left = right +1
        else:
            maxLen = max(maxLen, (right-left+1))
        right += 1
    return maxLen

nums = [0,1]
print(findMaxConsecutiveOnes(nums))

# Using count
def findMaxConsecutiveOnes(nums):
    left = 0
    maxLen = 0
    one_count = 0
    while left < len(nums):
        if nums[left] != 0:
            one_count += 1
            maxLen = max(maxLen, one_count)
        else:
            one_count = 0
        left += 1
    return maxLen

nums = [0,1]
print(findMaxConsecutiveOnes(nums))

################################################################################################################################################################
"""
487. Max Consecutive Ones II

You are given a binary array nums that contains only 0s and 1s. You need to find the maximum number of consecutive 1s that 
you can get if you are allowed to flip at most one 0 to 1.

For example, if you have the array [1, 0, 1, 1, 0], you can flip the first 0 to get [1, 1, 1, 1, 0], which gives you 4 consecutive 1s. 
Or you could flip the last 0 to get [1, 0, 1, 1, 1], which gives you 3 consecutive 1s. The maximum would be 4.

The key constraint is that you can flip at most one 0, meaning you can either flip exactly one 0 or flip no 0s at all. 
Your goal is to find the longest possible sequence of consecutive 1s after performing this operation optimally.

"""

def findMaxConsecutiveOnesII(nums):
    """
    Sliding window approach to find the maximum length of subarray with at most one zero flipped. 
    Time complexity: O(2n)
    Space complexity: O(1)
    """
    left = 0
    maxLen = 0
    zero_count = 0
    right = 0
    while right < len(nums):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        maxLen = max(maxLen, right - left + 1)
        right += 1
    return maxLen

nums = [1, 0, 1, 1, 0]
print(findMaxConsecutiveOnesII(nums))

def findMaxConsecutiveOnesIIOptimized(nums):
    """
    Sliding window approach to find the maximum length of subarray with at most one zero flipped. 
    Time complexity: O(n)
    Space complexity: O(1)
    """
    left = 0
    right = 0
    maxLen = 0
    zero = 0
    while right < len(nums):

        if nums[right] == 0:
            zero += 1
        if zero > 1:
            if nums[left] == 0: # [1, 0, 1, 1, 0, 1, 1, 1] assume l =0, r=4, in this case zero is 2, so we have to reduce by 1 and increase left by 1
                zero -= 1
            left += 1
        if zero <= 1:
            maxLen = max(maxLen, (right-left+1))
        right += 1

   
    return maxLen

nums = [1, 0, 1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnesIIOptimized(nums))
################################################################################################################################################################

"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

def longestOnes(nums, k):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

    left = 0
    right = 0
    maxLen = 0
    zero = 0

    while right < len(nums):

        if nums[right] == 0:
            zero += 1
        if zero > k:
            if nums[left] == 0:
                zero -= 1
            left += 1
        if zero <= k:
            maxLen = max(maxLen, (right-left+1))
        right += 1
    return maxLen

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums, k))