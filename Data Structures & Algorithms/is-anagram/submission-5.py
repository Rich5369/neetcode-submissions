# number of characters in strings are equal
# same letters appear same amount of times in each string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if string len != then return False
        if len(s) != len(t):
            return False

        #create a dictionary for storing character counts
        count = {}

        # search through string s// if letter does not exist in string: initialize it at 1// if exist +=1
        for char in s:
            count[char] = count.get(char, 0) + 1

        # search through string t // if character is in count -=1 // if not in count return False
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True