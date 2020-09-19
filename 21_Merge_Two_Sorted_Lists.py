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
        p = ListNode(0)
        res_p = p
        while(l1 and l2):
            if l1.val<l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p=p.next
        
        if l1:
            p.next = l1
        else:
            p.next =l2
        return res_p.next