class Solution:
    #neetcode
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    #greg
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap children
        root.left, root.right = root.right, root.left

        self.invertTree1(root.left)
        self.invertTree1(root.right)

        return root
    
    # time : O(n)
    # space: O(height) -> O(n)