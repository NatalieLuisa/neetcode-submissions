class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = {}
        for i in nums:
            if i not in maj:
                maj[i] = 1
            else:
                maj[i] +=1
        return max(maj, key = maj.get)
        """#for i, val in enumerate(nums)
        for i in nums:
            if i not in maj:
                maj.add(i)
            else:
                maj.get(i) + 1
        return max(maj(i))
"""