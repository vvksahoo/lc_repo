"""
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all 
the elements in the subarray is strictly less than k.


Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

"""

def numSubarrayProductLessThanK(nums, k):
    """
    Time Complexity: O(2n)
    Space Complexity: O(1)
    """
    left = 0
    right = 0
    product_of_subarray = 1
    no_subarray = 0

    while right < len(nums):
        product_of_subarray *= nums[right]

        while product_of_subarray >= k and left <= right:
            product_of_subarray /= nums[left]
            left += 1
        no_subarray += right - left + 1
        right += 1
    return no_subarray