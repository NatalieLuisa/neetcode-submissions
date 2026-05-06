class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res


"""class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted.nums()
        i, j, k = 0 , 1, len(nums)-1 
        hold = []
        while nums:
            res = nums[i] + nums[j] + nums[k]
            if res == 0 and res >= 0:
                k-=1
                hold.append(i, j, k )#n something like that i fo'rgoti how to return undencies 
            elif res =! 0 and res > 0:
                i+=1
                j+=1
            else:
                return   
        return       
"""








        