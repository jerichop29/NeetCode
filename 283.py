class Solution:
    def moveZeroes(nums):
        left = 0
        
        for right in range(len(nums)):
            # Check if the value of right pointer is zero.
            if nums[right] != 0:
                #Swap the value of left and right pointer
                nums[left], nums[right] = nums[right], nums[left]
                #increase the left pointer position.
                left += 1

            else:
                pass
                
        return nums
    
        
print(Solution.moveZeroes([0,1,0,3,5,1]))
                
                