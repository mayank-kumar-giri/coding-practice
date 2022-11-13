class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    indices = {}
    n = len(nums)
    for i in range(n):
      try:
        indices[nums[i]].append(i)
      except:
        indices[nums[i]] = [i]
    for i in range(n):
      diff = target - nums[i]
      if diff == nums[i]:
        if len(indices[nums[i]]) > 1:
          return indices[nums[i]][:2]
        else:
          continue
      try:
        return [indices[nums[i]][0], indices[diff][0]]
      except:
        continue
    return [-1,-1]