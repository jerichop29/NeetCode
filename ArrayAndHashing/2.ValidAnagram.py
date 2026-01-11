from collections import Counter

class Solution:
    def isAnagram(s, t):
        if Counter(s) != Counter(t):
            return False
        return True
    
#print(Solution.isAnagram("jar", "jam")) False
#print(Solution.isAnagram("racecar", "carrace")) True

