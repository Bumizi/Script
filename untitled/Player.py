class Player:
    UPPER = 6
    LOWER = 7
    def __init__(self, name):
        self.name = name
        self.scores=[0 for i in range(self.UPPER+self.LOWER)]
        self.used = [False for i in range(self.UPPER+self.LOWER)]

    def setScore(self, score, index):
        self.scores[index] = score
    def setAtUsed(self, index):
        self.used[index] = True
    def getUpperScore(self): #상위 6개 카테고리 점수의 합을 반환
        UpperScore = 0
        for i in range(self.UPPER):
            UpperScore += self.scores[i]
        return UpperScore
    def getLowerScore(self): #하위 7개 카테고리 점수의 합을 반환
        LowerScore = 0
        for i in range(self.UPPER, self.UPPER+self.LOWER):
            LowerScore += self.scores[i]
        return LowerScore
    def getUsed(self):
        pass
    def getTotalScore(self):
        if self.getUpperScore() >= 63:
            return self.getUpperScore() + self.getLowerScore() + 35
        else:
            return self.getUpperScore() + self.getLowerScore()

    def toString(self):
        return self.name

    def allLowerUsed(self):  # lower category 7개 모두 사용되었는가 ?
        for i in range(self.UPPER, self.UPPER+self.LOWER):
            if(self.used[i]==False):
                return False
        return True

    def allUpperUsed(self): #upper 6개 카테고리가 모두 사용되었는가? True of False  / UpperScores, UpperBonus 계산에 활용
        for i in range(self.UPPER):
            if(self.used[i]==False):
                return False
        return True