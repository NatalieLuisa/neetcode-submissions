class MedianFinder:

    def __init__(self):
        self.res = []

    def addNum(self, num: int) -> None:
        
        self.res.append(num)

        

    def findMedian(self) -> float:
        tot = len(self.res)
        self.res.sort()
      
        return (self.res[tot // 2] if (tot & 1) else
                (self.res[tot // 2] + self.res[(tot // 2 )- 1]) / 2)

        
        
        

        
        