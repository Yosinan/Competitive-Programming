class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sortedlist = []

        for i in range(len(nums)):
            for j in range(len(nums)):

                if nums[i] < nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                
