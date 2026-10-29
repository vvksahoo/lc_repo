"""
2460. Apply Operation to an Array
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.

Note that the operations are applied sequentially, not all at once.
Example 1:

Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]
Explanation: We do the following operations:
- i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
- i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,4,0,1,1,0].
- i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
- i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,2,0,0].
- i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,0,0].
After that, we shift the 0's to the end, which gives the array [1,4,2,0,0,0].
Example 2:

Input: nums = [0,1]
Output: [1,0]
Explanation: No operation can be applied, we just shift the 0 to the end.

"""
nums = [1,2,2,1,1,0]

def applyOperations(nums):

    for i in range(len(nums)-1):
        # operation
        if nums[i] == nums[i+1] and nums[i] !=0:
            nums[i] *= 2
            nums[i+1] = 0
    
    # shift non-zero to front
    non_zero_index = 0
    for i in nums:
        if i > 0:
            nums[non_zero_index] = i
            non_zero_index += 1
    nums[non_zero_index:] = [0] * (len(nums)-non_zero_index)
    return nums
    
# print(applyOperations(nums))

def applyOperationsOptimized(nums):
    """
    Approach:
    1. Traverse the input array from left to right.
    2. For each element, check if it is equal to the next element and not zero.
    3. If they are equal, double the current element and set the next element to zero.
    4. During this operation take another pointer to keep track of the position to shift non-zero elements, and swap elements as needed.
    5. Handle the case when the length of the array is 2 separately.
    """

    # handle the case of length is 2
    nums_size = len(nums)
    if nums_size == 2:
        if nums[0] == nums[1] and nums[0] != 0:
            nums[0] *= 2
            nums[1] = 0
        elif nums[0]==0:
            nums[0], nums[1] = nums[1], nums[0]
        return nums
    # handle the case when length is more than 2
    shift_non_zero_index = 0
    for i in range(nums_size):
        # apply operations
        if i < nums_size-1 and nums[i] == nums[i+1] and nums[i] !=0:
            nums[i] *= 2
            nums[i+1] = 0
        if nums[i] != 0:
            if i != shift_non_zero_index:
                nums[i], nums[shift_non_zero_index] = nums[shift_non_zero_index], nums[i]
            shift_non_zero_index+= 1
    return nums


def applyOperationOptimizedWay(nums):

        shift_non_zero_index = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                nums[shift_non_zero_index], nums[i] = nums[i], nums[shift_non_zero_index]
                shift_non_zero_index += 1
        # handle the last element
        if nums[-1] != 0:
            nums[shift_non_zero_index], nums[-1] = nums[-1], nums[shift_non_zero_index]
        return nums


"""
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

def removeElement(nums, val):

    non_target_element_index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[non_target_element_index] = nums[i]
            non_target_element_index += 1
    return non_target_element_index

nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))