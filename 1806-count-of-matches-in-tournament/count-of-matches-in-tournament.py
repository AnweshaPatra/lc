class Solution:
    def numberOfMatches(self, n: int) -> int:
        sm = 0
        m = 0
        while n != 1:
            m = n // 2
            n = n - m
            sm += m
        return sm
        