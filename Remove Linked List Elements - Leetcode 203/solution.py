#definition of singly linked list
#questions that i have: 
# i dont understand how linked list worked
# why return dummy.next?
# why do i need 2 pointers?

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            next = curr.next

            if curr.val == val:
                prev.next = next
            else:
                prev = curr
            curr = next
        return dummy.next 