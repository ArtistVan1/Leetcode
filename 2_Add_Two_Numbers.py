# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.getlength(l1)<self.getlength(l2):
            l1,l2 = l2,l1
        head = l1
        while l2:
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        p = head
        while(p):
            if p.val > 9:
                p.val -= 10
                if p.next:
                    p.next.val += 1
                else:
                    p.next = ListNode(1)
            p = p.next

        return head
            
    
    
    def getlength(self,l):
        a = 1
        while l:
            l = l.next
            a = a+1
        return a