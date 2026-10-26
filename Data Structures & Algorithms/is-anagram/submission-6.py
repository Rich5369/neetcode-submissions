class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        #search through s, if the character is not there then initialize to 1, if it is there + 1
        for char in s:
            count[char] = count.get(char, 0) + 1

        #search through t
        for let in t:
            if let not in count or count[let] == 0:
                return False

            count[let] -= 1
        return True