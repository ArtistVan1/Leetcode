class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        min_l=len(strs[0])
		
        for w in strs:
            min_l=min(min_l,len(w))
        #print(min_l)
        s = strs[0][0:min_l]
        #print(s)
        res=[]
        for index,item in enumerate(strs):
            a = 0
            for i in range(0,min_l):
                if item[i]==s[i]:
                    a +=1
                else:
                    break
            res.append(a)
        res.sort()
        return s[0:res[0]]