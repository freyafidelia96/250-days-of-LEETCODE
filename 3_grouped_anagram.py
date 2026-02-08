from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            res[sortedWord].append(word)

        return list(res.values())
      
"""

Alternative Approach: Using Character Count as Key (Hash Table)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        
"""  

if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Basic test case
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    # Test 2: Empty input
    print(solution.groupAnagrams([]))
    # Expected: []
    
    # Test 3: Single word
    print(solution.groupAnagrams(["hello"]))
    # Expected: [["hello"]]
    
    # Test 4: All anagrams
    print(solution.groupAnagrams(["abc", "bca", "cab"]))
    # Expected: [["abc", "bca", "cab"]]
    
    # res = defaultdict(list)
    
    # for word in ["eat", "tea", "tan", "ate", "nat", "bat"]:
    #   count = [0] * 26
    #   for chr in word:
    #     count[ord(chr) - ord('a')] += 1
      
    #   res[tuple(count)].append(word)
    # print(list(res.values()))
    