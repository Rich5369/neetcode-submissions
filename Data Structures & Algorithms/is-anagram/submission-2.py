class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #check string lengths
        if len(s) != len(t):
            return False
        
        #create empty dic to store char counts
        char_count = {}

        #loop through chars in s // if char exists, +1 // else initialize count to 1
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1


        #loop through chars in t // if it doesn't exist or it's count is 0, return false
        #otherwise, -1 from count
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            
            char_count[char] -= 1

        #return true
        return True