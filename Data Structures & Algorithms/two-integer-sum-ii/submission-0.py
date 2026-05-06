class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted 
        l , r = 0 , len(numbers)-1
        res = []
        while l < r:
            add = numbers[l] + numbers[r]
            if add < target:
                l+=1
            elif add > target:
                r-=1 
            else:
                return [l+1, r+1]
        