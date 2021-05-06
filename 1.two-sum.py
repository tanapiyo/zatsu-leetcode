#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# @lc code=start

from typing import List


class Solution:
    # brute force
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i]+nums[j] == target:
    #                 return i, j

    # hash table
    # tableにまずelementを入れて、二週目ループでtarget-nums[i]と同じ値が入っているかみる
    # こうするとlookupで、O(n)くらいですむ
    # 追加ループの中で探すとより早くなる
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if(nums[i] in dic):
                return[dic[nums[i]], i]
            else:
                dic[target-nums[i]] = i
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     dic = {}
    #     for i, n in enumerate(nums):
    #         if n in dic:
    #             return [dic[n], i]
    #         dic[target-n]=i
        # @lc code=end
