class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs: #sort through strings in strs
            count = [0] * 26 # setting each letter count at 0 
            
            for char in string:
                count[ord(char) - ord('a')] += 1

            result[tuple(count)].append(string)
        return list(result.values())