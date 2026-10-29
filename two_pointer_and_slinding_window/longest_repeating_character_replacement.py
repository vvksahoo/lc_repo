"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""

def characterReplacement(s, k):

    """
    T: O(n+n) x 26
    S: O(26) = O(1)
    """
    left = 0
    right = 0
    maxLen = 0
    unique_ch = {}
    max_freq = 0
    
    while right < len(s):
        unique_ch[s[right]] = unique_ch.get(s[right], 0) + 1
        max_freq = max(max_freq, unique_ch[s[right]])
        while ((right-left+1) - max_freq) > k:
            unique_ch[s[left]] -=1
            max_freq = 0
            for ch in  unique_ch:
                max_freq = max(max_freq, unique_ch[ch])
            left += 1
            
        if ((right-left+1) - max_freq) <= k:
            maxLen = max(maxLen, (right-left+1))
        right += 1
    return maxLen

def characterReplacementOptimized(s, k):

    """
    T: O(n)
    S: O(26) = O(1)
    Reinitialization of max_freq doesnt help because if we are at max_freq let say 3 and our lenght is 6 i.e 6-3 = 3,
    reducing max_freq to 2 will not help. because our length will increaing from 6 to 7 i.e 7-2 = 5 which is > k.
    
    """
    left = 0
    right = 0
    maxLen = 0
    unique_ch = {}
    max_freq = 0
    
    while right < len(s):
        unique_ch[s[right]] = unique_ch.get(s[right], 0) + 1
        max_freq = max(max_freq, unique_ch[s[right]])
        if ((right-left+1) - max_freq) > k:
            unique_ch[s[left]] -=1
            left += 1
            
        if ((right-left+1) - max_freq) <= k:
            maxLen = max(maxLen, (right-left+1))
        right += 1
    return maxLen

s = "AABABBA"
k = 1

print(characterReplacement(s, k))

######################################################
"""
2024. Maximize the Confusion of an Exam
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

 

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
 

Constraints:

n == answerKey.length
1 <= n <= 5 * 104
answerKey[i] is either 'T' or 'F'
1 <= k <= n

"""

def maxConsecutiveAnswers(answerKey, k):
    left = 0
    right = 0
    maxLen = 0
    unique_ch = {}
    max_freq = 0
    while right < len(answerKey):
        unique_ch[answerKey[right]] = unique_ch.get(answerKey[right], 0) + 1
        max_freq = max(max_freq, unique_ch[answerKey[right]])
        if (right-left+1) - max_freq > k:
            unique_ch[answerKey[left]] -= 1
            left += 1
        else:
            maxLen = max(maxLen, (right-left+1)) 
        
        right += 1
    return maxLen