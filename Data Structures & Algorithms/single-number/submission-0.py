class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        n = sorted(nums)
        for i in n:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return list(res)[0]