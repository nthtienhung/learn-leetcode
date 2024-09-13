

class Solution1:
    #neetcode solution
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] in closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    def isValid2(self, s: str) -> bool:
        hashmap = {")" : "(", "]" : "[", "}" : "{"}
        stk = []
        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                #something about too many closing bracket?
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False
        return not stk
    #time: O(n)
    
s = "()[]{}"
solution = Solution1()
print(solution.isValid(s))