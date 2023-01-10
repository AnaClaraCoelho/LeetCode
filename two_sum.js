/* https://leetcode.com/problems/two-sum/ 

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    answer = [];
    for(var i=0; i< nums.length; i++){
        var num = nums[i];
        for(var j=0; j<nums.length -1; j++){
            if(j == i){} 
            else{
                if(target == nums[i] + nums[j]){
                    if(!answer.includes(i)){
                        answer.push(i);
                    }
                    if (!answer.includes(j)){
                        answer.push(j);
                    }
                }
            }
        }
    }
    return answer;
};