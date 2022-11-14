#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
  def romanToInt(self, s: str) -> int:
    symbol_value_map = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
      'IV': 4,
      'IX': 9,
      'XL': 40,
      'XC': 90,
      'CD': 400,
      'CM': 900,
    }

    n = len(s)
    number = 0
    i = 0
    while i<=(n-1):
      try:
        number += symbol_value_map[s[i]+s[i+1]]
        i += 2
      except:
        number += symbol_value_map[s[i]]
        i += 1
    return number
        
# @lc code=end

