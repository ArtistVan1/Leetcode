class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        for i in range(0,len(s)):
            #print(s[i])
            if s[i]=='[' or s[i]=='(' or s[i]== '{':
                stack.append(s[i])
            else:
                if not stack or stack[-1] != mapping[s[i]]:
                    return False
                stack.pop()
        return len(stack)==0