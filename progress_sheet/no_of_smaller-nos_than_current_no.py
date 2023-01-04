class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newlist = []
        counter = 0

        for i in nums:
            for j in range(len(nums)):
                if i > nums[j]:
                    counter += 1
            newlist.append(counter)
            counter = 0
        
        return newlist