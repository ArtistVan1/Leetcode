# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res =[]
        for i in range(len(lists)):
            while(lists[i]):
                res.append(lists[i].val)
                lists[i]=lists[i].next
        
        res.sort()
        p=ListNode(0)
        res_p=p
        for i in range(len(res)):
            p.next=ListNode(res[i])
            p=p.next
        return res_p.next