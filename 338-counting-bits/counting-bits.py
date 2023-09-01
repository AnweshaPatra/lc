class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            if i%2 != 0:
                res.append(res[i//2] + 1)
            else:
                res.append(res[i//2])
        return res