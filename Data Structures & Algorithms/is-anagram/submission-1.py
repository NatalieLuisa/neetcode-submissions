class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #dictionary
        s1 , t2 = {},{}
        for n in s:
            if n not in s1:
                s1[n] = 1
            elif n in s1:
                s1[n] +=1
        for m in t:
            if m not in t2:
                t2[m] = 1
            elif m in t2:
                t2[m] +=1
        if s1 == t2:
            return True
        return False    

        