"""
2302. Count Subarrays With Score Less Than K

The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.

Example 1:

Input: nums = [2,1,4,3,5], k = 10
Output: 6
Explanation:
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, 
while we need scores strictly less than 10.

Example 2:

Input: nums = [1,1,1], k = 5
Output: 5
Explanation:
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.
"""

def countSubarrays(nums, k):
    left = 0
    right = 0
    no_subarray = 0
    
    while left < len(nums):
        
        right = left
        sum_of_subarray = 0
        while right < len(nums):
            score = 0
            sum_of_subarray = sum_of_subarray + nums[right]
            score = sum_of_subarray * (right - left + 1)
            if sum_of_subarray >= k or score >= k: break
            if score < k:
                no_subarray += 1
            right += 1
        left += 1
    return no_subarray

nums = [5,2,6,8,9,7] # [2,1,4,3,5]
k = 50 #10
print(countSubarrays(nums, k))

def countSubarrays(nums, k):
    """
    Solve using two pointer and sliding window
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = 0
    no_subarray = 0
    sum_subarray = 0

    while right < len(nums):
        sum_subarray = sum_subarray + nums[right]
        score = sum_subarray * (right - left + 1)
        while score >= k and left <= right:
            sum_subarray = sum_subarray - nums[left]
            left += 1
            score = sum_subarray * (right - left + 1)
        no_subarray = no_subarray + (right - left + 1)

        right +=1
    no_subarray
    

nums = [5,2,6,8,9,7] # [2,1,4,3,5]
k = 50 #10
print(countSubarrays(nums, k))

