class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []

        for i in range(len(arr)):
            if i == (len(arr) - 1):
                res.append(-1)
                return res
            else:
                res.append(max(arr[i+1:]))
        return res
    #neetcode solution
    #i dont understand shit????
    def replaceElements1(self, arr: List[int]) -> List[int]:
        #initial max = -1 
        #reverse iteration
        #newmax = max(oldmax, arr[i])

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
            