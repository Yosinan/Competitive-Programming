class Solution(object):
    def isPowerOfFour(self, n):
        """ 
        :type n: int
        :rtype: bool
        """
        print(n)
        if(n == 1):
            return True
        if(n % 4 != 0 or n <=0):
            return False
        
        return self.isPowerOfFour(n / 4)
