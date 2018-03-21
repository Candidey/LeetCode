# 不理解python中的int类型大小怎么计算
import sys
class Solution():
    def reverse(self, x):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        k = 1
        if x < 0:
            x = abs(x)
            k = -1

        a = int(str(x)[::-1])
        if a > INT_MAX or a < INT_MIN:
            return 0
        else:
            return k*a

demo = Solution()
print(demo.reverse(1534236469))
