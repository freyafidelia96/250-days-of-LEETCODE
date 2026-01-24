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