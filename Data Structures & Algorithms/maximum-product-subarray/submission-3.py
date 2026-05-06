class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = 1
        curmin = 1
        res = nums[0]

        for n in nums:
            temp = curmax * n
            curmax = max(n,curmin * n, n * curmax )
            curmin = min(n,temp, n * curmin)
            res = max(curmax,res)
        return res