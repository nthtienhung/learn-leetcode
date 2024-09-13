class Solution:
    #neetcode solution 1
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        #must convert listnode -> array because listnode can only traverse in 1 direction.
        while head:
            array.append(head.val)
            head = head.next
        
        l, r = 0, len(array) - 1
        while l <= r:
            if array[l] != array[r]:
                return False
            l += 1
            r -= 1
        return True