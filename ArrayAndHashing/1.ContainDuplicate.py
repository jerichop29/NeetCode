class Solution:
    def hasDuplicate(nums):
        #convert into a set to convert a duplicate values as one
        set = set(nums)
        
        #if the set is not equal to nums(list) meaning there is no duplicate else duplicate elements exist
        if set != nums:
            return False

        return True
    
#print(Solution.hasDuplicate([1,2,4])) False
#print(Solution.hasDuplicate([1,2,3,2,4])) True
            
        