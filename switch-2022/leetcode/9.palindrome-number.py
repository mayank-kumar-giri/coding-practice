#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
  def isPalindrome(self, x: int) -> bool:
    x = str(x)
    n = len(x)
    last = n//2
    first = (n//2) if (n % 2) == 0 else ((n//2) + 1)
    if (x[:last] == x[first:][::-1]):
      return True
    return False
        
# @lc code=end

