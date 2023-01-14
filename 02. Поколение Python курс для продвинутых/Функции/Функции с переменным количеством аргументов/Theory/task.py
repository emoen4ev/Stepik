'''

https://leetcode.com/problems/two-sum/description/

1. Two Sum
Easy
42.2K
1.4K
Companies

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        results = {}
        for idx in range(len(nums)):
            if target - nums[idx] in results:
                return [results[target - nums[idx]], idx]
            results[nums[idx]] = idx


# target = 9
# nums = [2, 7, 3, 1, 5, 11, 15]

# target = 0
# nums = [0, 4, 3, 0]

target = 0
nums = [-3, 4, 3, 90]

solution = Solution()
print(solution.twoSum(nums, target))