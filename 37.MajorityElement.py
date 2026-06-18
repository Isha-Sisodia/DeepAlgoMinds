# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
class Solution:
    def majorityElement(self, arr):
        #code here
        n = len(arr)//2
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num in freq:
            if freq[num] > n:
                return num
            
        return -1
                
