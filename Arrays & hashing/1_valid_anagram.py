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
    
    count = {}
    for i in range(len(s)):
        count[s[i]] = count.get(s[i], 0) + 1
        count[t[i]] = count.get(t[i], 0) - 1
    
    return all(v == 0 for v in count.values())

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

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Valid anagram
    print(solution.isAnagram("anagram", "nagaram"))  # Expected: True
    
    # Test 2: Not an anagram
    print(solution.isAnagram("rat", "car"))  # Expected: False
    
    # Test 3: Different lengths
    print(solution.isAnagram("a", "ab"))  # Expected: False
    
    # Test 4: Empty strings
    print(solution.isAnagram("", ""))  # Expected: True
    
    for i in range(10):
        print(i)
    
