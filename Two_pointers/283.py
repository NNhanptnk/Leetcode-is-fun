class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        # Imagine a snow ball rolling down the hill !
        # Using two pointers technique, a slow and a fast pointer
        # Squeeze the zero-es between the slow and fast pointer

        # Like this : [...,nums[left],0,0,0,0,0,0,nums[right],5,0,3,0,2,...]
        
        left_z = 0
        # Find the first zero
        while left_z < len(nums) and nums[left_z]!=0 : 
            left_z+=1
        right_z = left_z

        while right_z < len(nums):
            if nums[right_z]!=0:
                nums[left_z]=nums[right_z]
                nums[right_z]=0
                left_z+=1
            right_z+=1