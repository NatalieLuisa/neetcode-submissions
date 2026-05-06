class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        track = {}
        for n in nums:
            if n not in track:
                track[n] = 1
            else:
                track[n] += 1
        return max(track, key=track.get)