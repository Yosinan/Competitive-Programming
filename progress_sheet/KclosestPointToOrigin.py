class Solution(object):
    def kClosest(self, points, k):
        """ 
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        c = []
        mylist = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            z = math.sqrt(x**2 + y**2)
            c.append([z,x,y])
        c.sort()
        for i in range(0,k):
            mylist.append([c[i][1],c[i][2]])
        return mylist
        
         
         
        
