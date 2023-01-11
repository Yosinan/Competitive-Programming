class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        
        rearrangedlist = []

        l = 0  
        r = len(nums)-1
        
        while len(rearrangedlist) != len(nums):
            rearrangedlist.append(nums[l])
            l+=1

            if l<=r:
                rearrangedlist.append(nums[r])
                r -=1
        return rearrangedlist
            
                
                
            
           
            
                
            
                
            
            
            
           