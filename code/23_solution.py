# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return 
        
        def merge(l1, l2):
            ret = curr = ListNode(None)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return ret.next
        
        lists = collections.deque(lists)
        while len(lists) > 1:
            l1 = lists.popleft()
            l2 = lists.popleft()
            l3 = merge(l1, l2)
            lists.append(l3)
        return lists.pop()