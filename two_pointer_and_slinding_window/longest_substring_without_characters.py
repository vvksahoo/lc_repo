"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

def lengthOfLongestSubstring(s):
    """
    T: O(nxn) = O(n2)
    S: O(n)
    """
    left = 0
    right = 0
    maxLen = 0
    while left < len(s):
        unique_ch = {}
        while right < len(s):
            if s[right] in unique_ch: break
            unique_ch[s[right]] = 1
            maxLen = max(maxLen, right-left+1)
            right += 1
        left += 1
    return maxLen

def lengthOfLongestSubstringOptimized(s):
    """
    T: O(n)
    S: O(min(n, m)), where m is the size of the charset
    """
    left = 0
    right = 0
    maxLen = 0
    unique_ch = {} 

    while right < len(s):
        if s[right] in unique_ch and unique_ch[s[right]] >= left:
            left = unique_ch[s[right]] + 1
        unique_ch[s[right]] = right
        maxLen = max(maxLen, (right-left+1))
        right += 1

    return maxLen

s = "abcabcbb"
print(lengthOfLongestSubstring(s))