class Solution:
    def twoSum(nums, target):
        #dictionary initialization
        seen = {}
        
        #Use hashmap structure 
        for i, num in enumerate(nums): #get the key and value of list
            complementary = target - num #make a temporary variable to check if it exist

            #if complementary not exist in dictionary just add key and value
            if complementary not in seen:
                seen[num] = i
            #if exist display the value and current index  
            else:
                return [seen[complementary], i]

print(Solution.twoSum([3,4,5,6], 9)) #[0,3]