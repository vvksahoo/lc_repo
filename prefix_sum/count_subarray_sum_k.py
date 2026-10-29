"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.


Example 1

Input: nums = [1, 1, 1], k = 2

Output: 2

Explanation: In the given array [1, 1, 1], there are two subarrays that sum up to 2: [1, 1] and [1, 1]. Hence, the output is 2.

Example 2

Input: nums = [1, 2, 3], k = 3

Output: 2

Explanation: In the given array [1, 2, 3], there are two subarrays that sum up to 3: [1, 2] and [3]. Hence, the output is 2.

"""

def countSubarray(nums, k):
    
    left = 0
    number_subarray = 0
    
    while left < len(nums):
        
        right = left
        res = 0
        while right < len(nums):
            res = res + nums[right]
            if res == k:
                number_subarray += 1
            right += 1
        
        left += 1
    
    return number_subarray
    
nums = [1,2,3,-3,1,1,1,4,2,-3]
k = 3
print(countSubarray(nums, k))

def countSubarrayOptimized(nums, k):
    """
    This function uses a prefix sum and a hash map to count the number of subarrays
    whose sum equals to k in an optimized way.
    Time Complexity: O(n x logn)
    Space Complexity: O(n)
    """
    
    left = 0
    prefix_sum = 0
    prefix_sum_map = {0:1}
    number_subarray = 0
    
    while left < len(nums):
        prefix_sum = prefix_sum + nums[left]
        rem = prefix_sum - k
        number_subarray = number_subarray + prefix_sum_map.get(rem, 0)
        prefix_sum_map[prefix_sum] = prefix_sum_map.get(prefix_sum, 0) + 1
        left += 1
    
    return number_subarray
    
nums = [1,2,3,-3,1,1,1,4,2,-3]
k = 3
print(countSubarrayOptimized(nums, k))