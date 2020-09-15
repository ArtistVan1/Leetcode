class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_l = 0
        res = ""
		
		
        for i in range(0,len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1
            left, right = i, i + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1
				
				
				
        return res
                
                
        