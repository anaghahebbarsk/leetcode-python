"""
LeetCode 1: Two Sum
Approach: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""                                                                                                                                        class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            res = target - nums[i]
            if res in d:
                return d[res],i
            else:
                d[nums[i]] = i 
        