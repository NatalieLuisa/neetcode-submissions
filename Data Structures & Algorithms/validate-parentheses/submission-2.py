class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        res = []
        for c in s:
            if c in dic:
                if res and res[-1] == dic[c]:
                    res.pop()
                else:
                    return False

            else:
                res.append(c)

        return True if not res else False