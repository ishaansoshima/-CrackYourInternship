class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #attempt 1
        # c={}
        # r,mc=0,0
        # for n in nums:
        #     c[n]=1+c.get(n,0)
        #     r=n if c[n]>mc else r
        #     mx=max(c[n]mc)
        # return r
        
        #attemp 2
        r,c=0,0
        for n in nums:
           if c==n:
               r=n
           c+=(1 if n==r else -1)
           
        return r
        
           
       