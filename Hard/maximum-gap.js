/*
    https://leetcode.com/problems/maximum-gap/
    
    Input: nums = [3,6,9,1]
    Output: 3
    Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var maximumGap = function(nums) {
    nums.sort()
    var diff = 0
    var temp_diff = 0
    for (var i=0; i<nums.length; i++){
        console.log(i)
        temp_diff = nums[i+1] - nums[i]
        console.log(temp_diff)

        if(temp_diff > diff){
            diff = temp_diff
        }
    }
    return diff
};
