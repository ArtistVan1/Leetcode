class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        if not nums:
            return 0
        for each in nums:
            if nums[n]!=each:
                n +=1
                nums[n]=each
                
        return n+1
                