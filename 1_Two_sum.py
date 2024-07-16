class Solution(object):
    def twoSum(self,nums,target):
        hash={}
        for  i,n in enumerate(len(nums)):
            if (target-n) in hash:
                return [hash[target-n],i]
            hash[n]=i
        return []
    