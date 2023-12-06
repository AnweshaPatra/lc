class Solution:
    def totalMoney(self, n: int) -> int:
        sm = 0
        monday = 1
        while n > 0:
            for day in range(min(n, 7)):
                sm += (monday + day)
            n -= 7
            monday += 1
        return sm


        