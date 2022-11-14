def isPalindrome(x: int) -> bool:
  checker = []
  total = 0
  
  temp = x
  while temp != 0:
    print(temp, total)
    temp = temp
    total += 1
  print('total', total)
  i = 0
  temp = x
  while temp != 0:
    digit = temp % 10
    print(temp, digit, checker, i)
    if i<(total//2):
      checker.append(digit)
    else:
      if ((total % 2)==1) and (i == (total // 2)):
        pass
      elif not digit==checker.pop():
        return False
    temp = temp
    i += 1
  return True

x = int(input())
print(isPalindrome(x))