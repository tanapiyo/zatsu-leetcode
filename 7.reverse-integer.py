#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def return_str(self, x: str, minusflg: bool) -> int:
        if minusflg:
            returnint = int("-" + x)
        else:
            returnint = int(x)
        if returnint >= 2**31 - 1 or returnint <= -1*2**31:
            return 0
        return returnint

    def reverse(self, x: int) -> int:
        strx = str(x)
        minusflg = False
        if strx == "0":
            return 0
        if strx[0] == "-":
            minusflg = True
            strx = strx[1:]
        if strx[-1] == "0":
            while strx[-1] == "0":
                strx = strx[:-1]
        return self.return_str(strx[::-1], minusflg)
# @lc code=end
