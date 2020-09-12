class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        length = len(s)
        if x<0:
            return False
        if x==0:
            return True
        if len(s)%2==0:
            for i in range(0,length/2):
                if s[i]!=s[length-1-i]:
                    return False
                else:
                    continue
            return True
        else:
            for i in range(0,(length-1)/2):
                if s[i] !=s[length-1-i]:
                    return False
                else:
                    continue
            return True
                
            
        