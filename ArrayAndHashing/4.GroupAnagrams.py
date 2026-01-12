from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26  # assuming lowercase a–z
            for c in word:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(word)

        result = list(groups.values())
        result.sort(key=len)   # smallest groups first (optional)

        return result

s = Solution()
print(s.groupAnagrams(["cat", "tac", "pot", "top", "act"]))