from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      
      return Counter(s) == Counter(t)
      

"""
HashMap Counting Approach

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

Array Counting Approach

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    # Initialize an array of 26 zeros
    count = [0] * 26
    
    for i in range(len(s)):
        # ord() gets the ASCII value; subtracting ord('a') maps 'a'->0, 'b'->1, etc.
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
        
    # If it's an anagram, every index should have returned to zero
    for val in count:
        if val != 0:
            return False
            
    return True

"""