class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,temp):
            if len(temp) == len(nums):
                self.res.append(temp[:])
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(nums,temp)
                temp.pop()
        self.res = []
        dfs(nums,[])
        return self.res