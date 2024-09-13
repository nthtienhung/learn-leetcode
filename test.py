# #Replace Elements with Greatest Element on Right Side
# Input: 
arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
def replaceElements(arr) -> list:
    result = []
    for i in range(len(arr)):
        if(i == len(arr) - 1):
            result.append(-1)
        else:
            list1 = arr[i+1:len(arr)]
            max_element = max(list1)
            result.append(max_element)
    return result

print(replaceElements(arr))