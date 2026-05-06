class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()
        for i in nums:
            if i not in dupe:
                dupe.add(i)
            elif i in dupe:
                return True
             
        return False
         