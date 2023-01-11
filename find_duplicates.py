"""
    https://leetcode.com/problems/find-all-duplicates-in-an-array/
    
    Given an integer array nums of length n where all the integers 
    of nums are in the range [1, n] and each integer appears once or twice, 
    return an array of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        duplicates = []
        for index in range(len(nums)):
            if index + 1 < len(nums):
                if nums[index] == nums[index + 1]:
                    duplicates.append(nums[index])
        return duplicates