from collections import Counter #counter modules that counts the number of every character as key:value dictionary

class Solution:
    def isAnagram(s, t):
        #get the count of every character and compare if its equal
        if Counter(s) != Counter(t):
            return False
        return True
    
print(Solution.isAnagram("jar", "jam")) #False
print(Solution.isAnagram("racecar", "carrace")) #True

