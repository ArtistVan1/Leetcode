class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = ['']* min(numRows, len(s
		
        godown = False
        currow = 0
        for a in s:
            rows[currow] += a
            if currow ==0 or currow == numRows-1:
                godown = not godown
            if godown:
                currow = currow+1
            else:
                currow = currow-1
        return "".join(rows)
		
		
		