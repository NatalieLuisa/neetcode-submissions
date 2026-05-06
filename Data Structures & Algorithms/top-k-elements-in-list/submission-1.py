class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for key in nums:
            if key not in res:
                res[key] = 1 
            else:
                res[key] +=1

        
        sorted_nums = sorted(res, key = res.get, reverse = True )
        return sorted_nums[:k]