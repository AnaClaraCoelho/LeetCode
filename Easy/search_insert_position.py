""" 
    https://leetcode.com/problems/search-insert-position/

    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. If not, return the
    index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target in nums:
                return nums.index(target)
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)



"""
em js
var searchInsert = function(nums, target) {
    if (nums.includes(target)) {
        return nums.indexOf(target)
    }
    nums.push(target)
    nums.sort((a,b) => a-b)
    return nums.indexOf(target)
}
"""