def numIslands(self, grid: List[List[str]] ) -> int:
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))
        while q: 
            row, col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r,c) not in visit):
                    q.append((r,c))
                    visit.add(r,c)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit:
                bfs(r,c)
                islands += 1
    return islands

#valid anagram
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

#twosum
def twoSum(self,nums: List[int], target: int) -> List[int]:
    prevMap = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i 
    return

#maximum subarray
def maxSubArray(self, nums: List[int]) -> int:
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub

#two sum ii
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    #2 pointers, start and end
    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            # plus 1 because of exercise req
            return [l + 1,r + 1]
    return []

#house robber
#dynamic programming
#use array and sub array
def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    #[rob1, rob2, n, n+1]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

#merge 2 sorted list
#given 2 linked list, merge into 1 linked list
# must have original nodes

# create a dummy node 
# output -> dummy -> insert 
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next

#Best Time to Buy and Sell Stock
#left is buy, right is sell
def maxProfit(self, prices: List[int]) -> int:
    left,right = 0,1
    maxP = 0

    while right < len(prices): 
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right += 1
    return maxP

#merge sorted array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    merged = nums1[:m] + nums2[:n]

    sorted_array = sorted(merged)
    #must clear nums1 before extend it with another
    #nums1 = sorted_array doesn't work 
    nums1.clear()
    nums1.extend(sorted_array)
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #last index of nums1
    last = m + n - 1

    #merge in reversed order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else: 
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    #fill nums1 with leftover nums2 elements
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1
#solution 1
def isAnagram(self, s: str, t: str) -> bool:
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()

    if s_list == t_list:
        return True
    else:
        return False
#solution 2
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        #is use countT[c] and c is not in countT, will error 
        if countS[c] != countT.get(c, 0):
            return False
    return True        

#climbing stairs
#decision trees
#dynamic programming
#caching
#dfs
#fibonacci
def climbStairs(self, n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one


#is palindrome
def isPalindrome(self, head: ListNode) -> bool:
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True
#invert binary trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# #Replace Elements with Greatest Element on Right Side
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#this code is too slow, cant submit on leetcode
def replaceElements(self, arr: List[int]) -> List[int]:
    result = []
    for i in range(len(arr)):
        if(i == len(arr) - 1):
            result.append(-1)
        else:
            list1 = arr[i+1:len(arr)]
            max_element = max(list1)
            result.append(max_element)
    return result
#more optimized
def replaceElements(self, arr: List[int]) -> List[int]:
    #initial max = -1
    #reverse iteration
    #new max = max(oldmax, arr[i])

    rightMax = -1

    for i in range(len(arr) - 1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax
    return arr
#
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur
#happy number
def isHappy(self, n: int) -> bool:
    visit = set() #memory O(n)

    while n not in visit:
        visit.add(n)
        n = self.sumOfSquares(n)

        if n == 1:
            return True
    return False
def sumOfSquares(self, n: int) -> int:
    output = 0
    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        #// is integer division
        n = n // 10
    return output
#diameter Of Binary Tree
#solution 1
#i dont get it
def diameterOfBinaryTree(self, root):
    if root is None:
        return 0

    # The diameter of a tree is the maximum of the following quantities:
    # 1. The diameter of T’s left subtree.
    # 2. The diameter of T’s right subtree.
    # 3. The longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)
    lheight = self.height(root.left)
    rheight = self.height(root.right)

    ldiameter = self.diameterOfBinaryTree(root.left)
    rdiameter = self.diameterOfBinaryTree(root.right)

    return max(lheight + rheight, max(ldiameter, rdiameter))

def height(self, node):
    # Compute the height of a tree--the number of nodes
    # along the longest path from the root node down to
    # the farthest leaf node.
    if node is None:
        return 0
    return 1 + max(self.height(node.left), self.height(node.right))


#solution 2
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res[0]

#Search Insert Position - Binary Search - Leetcode 35
class Solution:
    def searchIndex(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l  = mid + 1
            if target < nums[mid]:
                r = mid - 1
        return l
    
#Valid Palindrome - Leetcode 125 - Python
def isPalindrome(self, s: str) -> bool:
    res = ""
    for c in s:
        if c.isalnum():
            res += c.lower()
    return res == res[::-1]

#solution 2
def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

#solution 3
def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not self.alphaNum(s[l]):
            l += 1
        while r > l and not self.alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
    l, r = l + 1, r - 1
    return True
def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

#Isomorphic Strings - Leetcode 205 - Python
def isIsomorphic(self, s: str, t: str) -> bool:
    mapST, mapTS = {}, {}

    for c1, c2 in zip(s, t):
        if ((c1 in mapST and mapST[c1] != c2) or
            (c2 in mapTS and mapTS[c2] != c1)):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True

#191. Number of 1 Bits

#solution 1: must use submit to be see correct on leetcode 
def hammingWeight(self, n: int) -> int:
    if n < 0 or n > 2147483647:
        return "invalid input"
    totalOf1bits = 0
    binary0b = bin(n)
    binary = binary0b[2::]
    for c in binary:
        if c == '1' :
            totalOf1bits += 1
    return totalOf1bits

#solution 2
def hammingWeight(self, n: int) -> int:
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res


#Kth Largest Element in a Stream - Leetcode 703 - Python
#too difficult. cant do it

#Remove Duplicates from Sorted List - Leetcode 83 - Python
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head

    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next
    return head