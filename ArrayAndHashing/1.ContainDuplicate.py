class Solution():
    def hasDuplicate(nums):
        seen = set(nums)

        if seen != nums:
            return False

        return True
    
#print(Solution.hasDuplicate([1,2,4])) False
#print(Solution.hasDuplicate([1,2,3,2,4])) True
            
        