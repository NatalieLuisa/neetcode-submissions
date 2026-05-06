class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i == 'C':
                res.pop()
            elif i == '+':
                add = res[-1] + res[-2]
                #add = sum(res)
                res.append(add)
            elif i == 'D':
                mult = res[-1] * 2
                res.append(mult)
            else:
                res.append(int(i))
        return sum(res)

