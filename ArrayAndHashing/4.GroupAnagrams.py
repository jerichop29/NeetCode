from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        groups = defaultdict(list)

        #access every string in collection
        for str in strs:
            #create a list for key with 26 elements with 0 value
            key = [0] * 26

            #modified the key that represent number of every character in string
            for c in str:
                key[ord(c) - ord('a')] += 1  #every character count will increasee by 1 in the represetation
            groups[tuple(key)].append(str) #add in the dictionary the group is based on key

        #Convert the dictionary into a list, get the values, and sort based on length    
        result = list(groups.values())
        result.sort(key=len)
        
        return result
        

s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))