"""
1869. Longer Contiguous Segments of Ones than Zeros
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous 
segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
Example 2:

Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.
Example 3:

Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
 

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
"""

def checkZeroOnes(s: str) -> bool:
    maxOnes = 0
    maxZeros = 0
    currentOnes = 0
    currentZeros = 0

    for char in s:
        if char == '1':
            currentOnes += 1
            maxOnes = max(maxOnes, currentOnes)
            currentZeros = 0
        else:
            currentZeros += 1
            maxZeros = max(maxZeros, currentZeros)
            currentOnes = 0

    return maxOnes > maxZeros

s = "110100010"
print(checkZeroOnes(s))

# using pointer
def checkZeroOnes(s: str) -> bool:
    """
    Intuition: We need to find the longest contiguous segments of 1's and 0's in the binary string.
    Approach:
    We will use two pointers to find the maximum length of contiguous segments of 1's and 0's.
    """
    leftZero = 0
    leftOne = 0
    maxZero = 0
    maxOne = 0
    right = 0
    while right < len(s):
        
        if s[right] == "0":
            leftOne = right + 1
        else:
            maxOne = max(maxOne, (right-leftOne+1)) 
        if s[right] == "1":
            leftZero = right + 1
        else:
            maxZero = max(maxZero, (right-leftZero+1))   
        right += 1
    return maxOne > maxZero

s = "110100010"
print(checkZeroOnes(s))


#######################################################################################################
"""
1784. Check if Binary String Has at Most One Segment of Ones
Given a binary string s ​​​​​wit leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.


Example 1:

Input: s = "1001"
Output: false
Explanation: The string has two segments of size 1.
Example 2:

Input: s = "110"
Output: true

Input: s = "0110"
Output: true

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.

"""

def checkOnesSegment(s):
    seen_zero = False
    for ch in s:
        if ch == "0":
            seen_zero = True
        elif seen_zero:
            return False
    return True

s = "1001"
print(checkOnesSegment(s))


def checkOnesSegment(s):
    # In case the question says with leading zero then solution would be

    seen_zero_after_one = False
    seen_first_one = False

    for ch in s:
        if ch == '0':
            if seen_first_one:
                seen_zero_after_one = True
        else:
            seen_first_one = True
            if seen_zero_after_one:
                return False
    return True


   

s = "01001"
print(checkOnesSegment(s))