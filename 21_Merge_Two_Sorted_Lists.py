# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=[]
        while(l1):
            res.append(l1.val)
            l1=l1.next
        while(l2):
            res.append(l2.val)
            l2=l2.next
        res.sort()
        print(res)
        p=ListNode(0)
        res_p = p
        for i in range(0,len(res)):
            p.next = ListNode(res[i])
            p = p.next
        return res_p.next