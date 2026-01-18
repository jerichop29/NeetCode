class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        print(arr)
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

s = Solution()
print(s.topKFrequent([1,1,1,1,1,2,2,2,2,2,2,3,3], 2))