"""
Given an array arr[] of size n containing integers, the task is to find the length of the longest subarray having sum equal to the given value k.

Note: If there is no subarray with sum equal to k, return 0.

"""

def longestSubarray(nums, k):
    """
    Time: O(nx2)
    Space: O(1)
    """
    left = 0
    maxLen = 0
    size = len(nums)

    while left < size:

        right = left
        count = 0
        while right < size:
            count = count + nums[right]
            if count == k:
                maxLen = max(maxLen, (right - left + 1))
            elif count > k: break
            right += 1

        left += 1
    return maxLen

nums = [1,2,3,1,1,1,1,4,2,3]
k = 3

print(longestSubarray(nums, k))

# incase of only zero and negative numbers in nums we can use below approach to better solution

def longestSubarrayBetter(nums, k):
    """
    Intuition:
    The idea is to use a prefix sum with a hash map to efficiently find the longest subarray with sum k, even when the array contains negative numbers or zeros.

    As you iterate through the array, you keep a running sum (count).
    For each index, you check:
        If the current prefix sum equals k, the subarray from the start to this index is a candidate.
        If there exists a previous prefix sum such that current_sum - previous_sum = k, then the subarray between those indices sums to k.
        The hash map (unique_sum) stores the first occurrence of each prefix sum, allowing you to quickly check if such a subarray exists and calculate its length.
        This approach works for all integer arrays, including those with negative numbers.

    Time Complexity
    O(n log n): Each element is processed once. All hash map operations (insert and lookup) are O(1) on average. log n is unordered_map
    Space Complexity
    O(n): In the worst case, the hash map stores a prefix sum for each index.
    
    """

    left = 0
    count = 0
    maxLen = 0
    unique_sum = {}
    while left < len(nums):
        
        count = count + nums[left]
        if count == k:
            maxLen = max(maxLen, left + 1)
        if (count - k) in unique_sum:
            maxLen = max(maxLen, (left - unique_sum[count - k]))
        if count not in unique_sum:
            unique_sum[count] = left

        left += 1
    return maxLen




# incase of only positive numbers in nums we can use two pointer to have a better approach
def longestSubarrayPositiveOptimized(nums, k):
    """
    Time: O(2n)
    Space: O(1)
    if array contains positive and zero than this would be the optimal solution
    """
    left = 0
    maxLen = 0
    size = len(nums)
    right = 0
    count = 0

    while right < size:

        count = count + nums[right]
        # left should in the left or less than right because then only we can consider that a subarray or a valid window
        while left < right and count > k:

            count = count - nums[left]
            left += 1
        if count == k:
            maxLen = max(maxLen, (right - left + 1))

        right += 1

   
    return maxLen