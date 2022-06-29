class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        result = [-1, -1]
        for i in range(len(nums)):
            if nums[start] == target and start >= 0:
                result[0] = start
                start = -1
            else:
                start = start + 1
            if nums[end] == target and end >= 0:
                result[1] = end
                end = -1
            else:
                end = end - 1

        return result