class Solution:
  def romanToInt(self, s:str) -> int:
    maps = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
  }

    sums = maps[s[len(s)-1]]

    for i in range(len(s)-2, -1, -1):
      if maps[s[i]] >= maps[s[i+1]]:
        sums += maps[s[i]]
      else:
        sums -= maps[s[i]]
     
    return sums