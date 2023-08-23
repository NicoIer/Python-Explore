class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # 用于记录x的反转数
        m = 0
        # 用于记录x的原始值
        y = x
        while x:
            m = m * 10 + x % 10
            x //= 10
        return m == y