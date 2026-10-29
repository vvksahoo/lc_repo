"""
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

"""

def totalFruitBruteForce(fruits):
    """ 
    T: O(nx2)
    S: O(3)
    """
    left = 0
    maxLen = 0

    while left < len(fruits):
        right = left
        unique_ch = set()
        while right < len(fruits):
            unique_ch.add(fruits[right])
            if len(unique_ch) > 2: break
            maxLen = max(maxLen, (right-left+1))

            right += 1

        left += 1
    return maxLen

fruits = [1,2,3,2,2]
print(totalFruitBruteForce(fruits))

def totalFruitBetterThanBruteForce(fruits):
    """
    T: O(n+n)
    S: (3)
    
    """
    left = 0
    right = 0
    maxLen = 0
    unique_ch = {}

    while right < len(fruits):

        unique_ch[fruits[right]] = unique_ch.get(fruits[right], 0) + 1

        if len(unique_ch.keys()) <= 2:
            maxLen = max(maxLen, (right - left + 1))
        else:
            while len(unique_ch.keys()) > 2:
                unique_ch[fruits[left]] -= 1
                if unique_ch[fruits[left]] <= 0:
                    del unique_ch[fruits[left]]
                left += 1


        right += 1
    return maxLen

def totalFruitOptimized(fruits):

    left = 0
    right = 0
    maxLen = 0
    unique_ch = {}

    while right < len(fruits):

        unique_ch[fruits[right]] =  unique_ch.get(fruits[right], 0) + 1

        if len(unique_ch.keys()) <= 2:
            maxLen = max(maxLen, (right - left + 1))
        else:
            unique_ch[fruits[left]] -= 1
            if unique_ch[fruits[left]] <= 0:
                del unique_ch[fruits[left]]
            left += 1

        right += 1
    return maxLen




