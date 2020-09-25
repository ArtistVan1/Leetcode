class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = nums[0]
        sums = 0
        
        for num in nums:
            sums +=num
            if sums >max_value:
                max_value = sums
            if sums <0:
                sums = 0
        
        return max_value
        