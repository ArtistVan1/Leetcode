class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        #把num1,num2翻转方便计算
        num1 = num1[::-1]; num2 = num2[::-1]
        #每一位互相乘的结果用一维数组去储存
        arr = [0 for i in range(len(num1)+len(num2))]
        #填充这个一维数组
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])
        ans = []
        #计算每一位的终极结果
        for i in range(len(arr)):
            #digit表示这一位的数字
            digit = arr[i] % 10
            #carry表示加给下一位的量
            carry = arr[i] / 10
            if i < len(arr)-1:
                #下一位加上
                arr[i+1] += carry
            #更新答案
            ans.insert(0, str(digit))
        #去除首位为0的情况
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        #连接成字符串
        return ''.join(ans)
		
		
		
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1,num2 = num1[::-1], num2[::-1]
        arr = [0 for i in range(len(num1)+len(num2))]
        ans = []
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i])*int(num2[j])
        for i in range(len(arr)):
            dig = arr[i]%10
            carry = arr[i]/10
            if i<len(arr)-1:
                arr[i+1] +=carry
            ans.insert(0,str(dig))
        
        while ans[0]=='0' and len(ans)>1:
            del ans[0]
        return ''.join(ans)
            