# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i,num in enumerate(numbers):
            r = target - num
            if r in h:
                return [h[r] + 1, i + 1]   
            h[num] = i
'''another better solution based on binary search 
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
'''
        