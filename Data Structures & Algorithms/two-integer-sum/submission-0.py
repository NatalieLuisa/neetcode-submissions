class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, n in enumerate(nums):
            dif = target - n 
            if dif in x:
                return [x[dif], i]
            x[n] = i 