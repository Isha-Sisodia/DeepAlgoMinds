# https://www.geeksforgeeks.org/problems/value-equal-to-index-value1330/1

class Solution:
    def valEqualToPos(self, arr):
        ans = []
        for i in range(len(arr)):
            if arr[i] == i+1:
                ans.append(arr[i]) #ans.append(i+1)
        return ans
        
