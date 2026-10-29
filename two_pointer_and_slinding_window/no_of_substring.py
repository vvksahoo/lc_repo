"""
1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

"""


def numberOfSubstrings(s):
    left = 0
    maxSubstring = 0

    while left < len(s):
        right = left
        seen_ch = set()
        while right < len(s):
            seen_ch.add(s[right])
            if len(seen_ch) == 3:
                maxSubstring += 1
                break
            right += 1
        left += 1

def numberOfSubstringsOptimized(s):
    right = 0
    maxSubstring = 0
    last_seen = {"a": -1, "b": -1, "c": -1}

    while right < len(s):
        last_seen[s[right]] = right
        if last_seen["a"] != -1 and last_seen["b"] != -1 and last_seen["c"] != -1:
            maxSubstring = maxSubstring + (min(last_seen["a"], last_seen["b"], last_seen["c"])) + 1
        right += 1
    return maxSubstring

def numberOfSubstringsOptimized(s):
    right = 0
    maxSubstring = 0
    seen_a = -1
    seen_b = -1
    seen_c = -1

    while right < len(s):
        if s[right] == "a":
            seen_a = right
        elif s[right] == "b":
            seen_b = right
        else:
            seen_c = right
        maxSubstring = maxSubstring + min(seen_a, seen_b, seen_c) + 1
        right += 1
    return maxSubstring

s = "abcabc"
print(numberOfSubstrings(s)) # 10

def numberOfSubstringsOptimized(s):
    left = 0
    maxSub = 0
    right = 0
    dct = dict()
    while right < len(s):
        dct[s[right]] = 1
        if len(dct) == 3:
            maxSub = maxSub + len(s) - right + 1
            del dct[left]
            left += 1
        right +=1

    return maxSub