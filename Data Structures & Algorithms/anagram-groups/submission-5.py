from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list) #O(1)
        for s in strs: # O(n)
            count = [0] * 26 # O(1)
            for c in s: # O(m)
                count[ord(c) - ord("a")] += 1 #ord gives ascii value
            
            key = tuple(count)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())

        # Time:  O(n * m) Space: (n * m)