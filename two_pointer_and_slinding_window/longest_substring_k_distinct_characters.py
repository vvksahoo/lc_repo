"""
340. Longest Substring with At Most K Distinct Characters

You are given a string s and an integer k. Your task is to find the length of the longest substring 
within s that contains at most k distinct characters.

A substring is a contiguous sequence of characters within the string. 
For example, if s = "eceba" and k = 2, you need to find the longest substring that has no more than 2 different characters.

"""

def lengthOfLongestSubstringKDistinct(s, k):
    left = 0
    right = 0
    maxLen = 0
    unique_ch = {}
    
    while left < len(s):
        right =  left
        unique_ch = set()
        while right < len(s):
            unique_ch.add(s[right])
            if len(unique_ch) <= k:
               maxLen = max(maxLen, (right-left+1))
            else:
                break
            right += 1
        left += 1
    return maxLen


s = "eceba"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))


def lengthOfLongestSubstringKDistinctOptimized(s, k):
    left = 0
    right = 0
    maxLen = 0
    unique_ch = {}
    
    while right < len(s):
        unique_ch[s[right]] = unique_ch.get(s[right], 0) + 1
        if len(unique_ch) <= k:
           maxLen = max(maxLen, (right-left+1))
        else:
            unique_ch[s[left]] -= 1
            if unique_ch[s[left]] <= 0:
                del unique_ch[s[left]]
            left += 1
        right += 1
    return maxLen
