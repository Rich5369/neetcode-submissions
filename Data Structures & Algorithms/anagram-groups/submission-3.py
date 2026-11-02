from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 #creates new list for letters a-z 0-25
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())