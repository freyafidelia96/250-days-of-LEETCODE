from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      
      return Counter(s) == Counter(t)
      

"""

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