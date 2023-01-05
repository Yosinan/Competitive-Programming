class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mylist = []

        nums.sort()

        for i in range(len(nums)):
            if target == nums[i]:

                 mylist.append(i)
                 
        return mylist    
                 

                