# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # a dummy node to point to the head element
        flist = ListNode()
        # local variables to advance lists
        f = flist
        n = list1
        m = list2
        # while loop compares the elements in the list 
        # and adds the smaller to f
        # note: both lists need to be non-empty
        while n != None and m != None:
            if n.val <= m.val:
                f.next = ListNode(val=n.val)
                f = f.next
                n = n.next
            else:
                f.next = ListNode(val=m.val)
                f = f.next
                m = m.next
        # check if list1 has anything left
        while n != None:
            f.next = ListNode(val=n.val)
            n = n.next
            f = f.next
        # check if list2 has anything left
        while m != None:
            f.next = ListNode(val=m.val)
            m = m.next
            f = f.next
        return flist.next