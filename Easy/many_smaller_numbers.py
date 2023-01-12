"""
    https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

    Given the array nums, for each nums[i] find out how many numbers in the array are 
    smaller than it. That is, for each nums[i] you have to count the number of valid j's
     such that j != i and nums[j] < nums[i].

    Return the answer in an array.
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        answer = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            answer.append(count)
        return answer