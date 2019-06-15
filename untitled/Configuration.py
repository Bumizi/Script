from Dice import *
class Configuration:
    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes", "Upper Scores","Upper Bonus(35)",
               "Three of a kind", "Four of a kind", "Full House(25)", "Small Straight(30)", "Large Straight(40)",
               "Yahtzee(50)","Chance","Lower Scores", "Total"]
    def getConfigs(self):   # 정적 메소드 : 객체생성 없이 사용 가능
        return Configuration.configs
    def score(row, d):  # 정적 메소드 : 객체생성 없이 사용 가능
        # row 에 따라 주사위 점수를 계산 반환 . 예를 들어 , row 가 0 이면 " Ones" 가 채점되어야 함을 의미합니다 .
        # row 가 2 이면 , " Threes" 가 득점되어야 함을 의미합니다 .
        # row 가 득점 ( scored ) 하지 # 않아야 하는 버튼 ( 즉 , UpperScore , UpperBonus , LowerScore , Total 등 ) 을 나타내는 경우
        # - 1 을 반환합니다 .
        if (row>=0 and row<=6):
            return Configuration.scoreUpper(d, row + 1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row == 10):
            return Configuration.scoreFullHouse(d)
        elif (row == 11):
            return Configuration.scoreSmallStraight(d)
        elif (row == 12):
            return Configuration.scoreLargeStraight(d)
        elif (row == 13):
            return Configuration.scoreYahtzee(d)
        elif (row == 14):
            return Configuration.sumDice(d)
        return 0

    def scoreUpper(d, num):  # 정적 메소드 : 객체생성 없이 사용 가능
        # Upper Section 구성 ( Ones , Twos , Threes , ...) 에 대해 주사위 점수를 매 깁니다 . 예를 들어 ,
        # num 이 1 이면 " Ones" 구성의 주사위 점수를 반환합니다
        result = 0
        if (num == 1):
            for i in d:
                if i.roll == 1:
                    result += 1
            return result
        elif (num == 2):
            for i in d:
                if i.roll == 2:
                    result += 2
            return result
        elif (num == 3):
            for i in d:
                if i.roll == 3:
                    result += 3
            return result
        elif (num == 4):
            for i in d:
                if i.roll == 4:
                    result += 4
            return result
        elif (num == 5):
            for i in d:
                if i.roll == 5:
                    result += 5
            return result
        elif (num == 6):
            for i in d:
                if i.roll == 6:
                    result += 6
            return result
        return result

    def scoreThreeOfAKind(d):
        check = []
        for i in d:
            check.append(i.roll)
        for i in range(1, 7):
            if check.count(i) >= 3:
                result = sum(check)
                return result
        return 0

    def scoreFourOfAKind(d):
        check = []
        for i in d:
            check.append(i.roll)
        for i in range(1, 7):
            if check.count(i) >= 4:
                result = sum(check)
                return result
        return 0

    def scoreFullHouse(d):
        check = []
        if_2 = False
        if_3 = False
        for i in d:
            check.append(i.roll)
        for i in range(1, 7):
            if check.count(i) == 2:
                if_2 = True
            elif check.count(i) == 3:
                if_3 = True
        if if_2 and if_3:
            return 25
        return 0

    def scoreSmallStraight(d):
        #1 2 3 4  혹은 2 3 4 5 혹은 3 4 5 6 검사
        #1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
        check = []
        for i in d:
            check.append(i.roll)
        if (check.count(1) >= 1) and (check.count(2) >= 1) and (check.count(3) >= 1) and (check.count(4) >= 1):
            return 30
        if (check.count(2) >= 1) and (check.count(3) >= 1) and (check.count(4) >= 1) and (check.count(5) >= 1):
            return 30
        if (check.count(3) >= 1) and (check.count(4) >= 1) and (check.count(5) >= 1) and (check.count(6) >= 1):
            return 30
        return 0

    def scoreLargeStraight(d):
        # 1 2 3 4 5 혹은 2 3 4 5 6 검사
        check = []
        for i in d:
            check.append(i.roll)
        if (check.count(1) >= 1) and (check.count(2) >= 1) and (check.count(3) >= 1) and (check.count(4) >= 1) and (check.count(5) >= 1):
            return 40
        if (check.count(2) >= 1) and (check.count(3) >= 1) and (check.count(4) >= 1) and (check.count(5) >= 1) and (check.count(6) >= 1):
            return 40
        return 0

    def scoreYahtzee(d):
        check = []
        for i in d:
            check.append(i.roll)
        for i in range(1, 7):
            if check.count(i) == 5:
                return 50
        return 0

    def sumDice(d):
        check = []
        for i in d:
            check.append(i.roll)
        result = sum(check)
        return result
