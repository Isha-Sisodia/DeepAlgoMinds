# https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=eeudwo2i
# Brute force (Accepted) 
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# Optimised (Accepted)
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]] = i
        
