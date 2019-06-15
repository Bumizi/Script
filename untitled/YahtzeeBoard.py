from tkinter import *
from tkinter import font
import  tkinter.messagebox
from Player import *
from Dice import *
from Configuration import *

class YahtzeeBoard:
    UPPERTOTAL = 6  #UpperScores의 인덱스 (6번째)
    UPPERBONUS = 7  #UpperBonus의 인덱스 (7번째)
    LOWERTOTAL = 15 #LowerScores의 인덱스 (15번째)
    TOTAL = 16  #Total의 인덱스 (16번째)
    dice = []
    diceButtons = []
    fields = []
    players = []
    numPlayers = 0
    player = 0
    round = 0
    roll = 0
    def __init__(self):
        self.InitPlayers()
    def InitPlayers(self):
        self.pwindow = Tk()
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.label=[]
        self.entry=[]
        self.label.append(Label(self.pwindow, text='플레이어 명수', font=self.TempFont))
        self.label[0].grid(row=0, column=0)
        for i in range(1, 11):
            self.label.append(Label(self.pwindow, text='플레이어'+str(i)+' 이름', font=self.TempFont))
            self.label[i].grid(row=i, column=0)
        for i in range(11):
            self.entry.append(Entry(self.pwindow, font=self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text='Yahtzee 플레이어 설정 완료', font=self.TempFont, command=self.playerNames).grid(row=11, column=0)
        self.pwindow.mainloop()
    def playerNames(self):
        self.numPlayers = int(self.entry[0].get())
        for i in range(1, self.numPlayers+1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()
        self.initInterface()
    def initInterface(self):
        self.window = Tk("Yahtzee Game")
        self.window.geometry("1600x800")
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        for I in range(5): # Dice 객체 5 개 생성
            self.dice.append(Dice())
        self.rollDice = Button(self.window, text="Roll Dice", font = self.TempFont, command = self.rollDiceListener)
        self.rollDice.grid(row=0, column=0)

        for i in range(5):    # dice 버튼 5 개 생성
            self.diceButtons.append(Button(self.window, text="?", font=self.TempFont, width=8, command=lambda row=i: self.diceListener(row)))
            # 각각의 dice 버튼에 대한 이벤트 처리 diceListener 연결
            # 람다 함수를 이용하여 diceListener 매개변수 설정하면 하나의 Listener 로 해결
            self.diceButtons[i].grid(row=i + 1, column=0)

        for i in range(self.TOTAL + 2):  # i 행 : 점수
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers):  # j 열 : 플레이어
                if (i == 0):  # 플레이어 이름 표시
                    Label(self.window, text=self.players[j].toString(), font=self.TempFont).grid( row=i, column=2 + j)
                else:
                    if (j==0): # 각 행마다 한번씩 리스트 추가 , 다중 플레이어 지원
                        self.fields.append(list())
                    #i - 1 행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정 , 매개변수 설정
                    self.fields[i-1].append(Button(self.window, text="", font=self.TempFont, width=8, command=lambda row=i-1: self.categoryListener(row)))
                    self.fields[i-1][j].grid(row=i,column=2 + j)
                    # 누를 필요없는 버튼은 disable 시킴
                    if (j != self.player or (i-1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS or (i-1) == self.LOWERTOTAL or (i-1) == self.TOTAL):
                        self.fields[i-1][j]['state'] = 'disabled'
                        self.fields[i-1][j]['bg'] = 'light gray'
        # 상태 메시지 출력
        self.bottomLabel=Label(self.window, text=self.players[self.player].toString()+ "차례: Roll Dice 버튼을 누르세요", width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.TOTAL + 2, column=0)
        self.window.mainloop()

    def rollDiceListener(self):    # rollDiceListener
        for i in range(5):
            if (self.diceButtons[i]['state'] != 'disabled'):
                self.dice[i].rollDice()
                self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))
        if (self.roll == 0 or self.roll == 1):
            self.roll += 1
            self.rollDice.configure(text="Roll Again")
            self.bottomLabel.configure(text="보관할 주사위 선택 후 Roll Again")
        elif (self.roll == 2):
            self.bottomLabel.configure(text="카테고리를 선택하세요")
            self.rollDice['state'] = 'disabled'
            self.rollDice['bg'] = 'light gray'

    def diceListener(self, row): # DiceListener
        self.diceButtons[row]['state'] = 'disabled'
        self.diceButtons[row]['bg'] = 'light gray'

    def categoryListener(self, row): # categoryListener
        score = Configuration.score(row, self.dice)  # 점수 계산
        index = row
        if (row>7):
            index = row-2
        # 선택한 카테고리 점수 적고 disable 시킴
        self.players[self.player].setScore(score, index)
        self.players[self.player].setAtUsed(index)
        self.fields[row][self.player].configure(text=str(score))
        self.fields[row][self.player]['state'] = 'disabled'
        self.fields[row][self.player]['bg'] = 'light gray'
        # UPPER category 가 전부 사용되었으면 UpperScore , UpperBonus 계산
        if (self.players[self.player].allUpperUsed()):
            self.fields[self.UPPERTOTAL][self.player].configure(text=str(self.players[self.player].getUpperScore()))
            if (self.players[self.player].getUpperScore() > 63):
                self.fields[self.UPPERBONUS][self.player].configure(text="35") #UPPERBONUS=7
            else:
                self.fields[self.UPPERBONUS][self.player].configure(text="0") #UPPERBONUS=7
        # LOWER category 전부 사용되었으면 LowerScore 계산
        if (self.players[self.player].allLowerUsed()):
            self.fields[self.LOWERTOTAL][self.player].configure(text=str(self.players[self.player].getLowerScore()))
        # UPPER category 와 LOWER category 가 전부 사용되었으면 TOTAL 계산
        if (self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed()):
            self.fields[self.TOTAL][self.player].configure(text=str(self.players[self.player].getTotalScore()))
        # 다음 플레이어로 넘어가고 선택할 수 없는 카테고리들은 disable 시킴
        self.player = (self.player + 1) % self.numPlayers
        for i in range(self.TOTAL+1):
            for j in range(self.numPlayers):
                # 누를 필요없는 버튼은 disable 시킴
                if (j != self.player or (i-1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS or (i-1) == self.LOWERTOTAL or (i-1) == self.TOTAL):
                    self.fields[i-1][j]['state'] = 'disabled'
                    self.fields[i-1][j]['bg'] = 'light gray'
                else:
                    for k in range(6):
                        if self.players[self.player].used[k] == False:
                            self.fields[k][j]['state'] = 'normal'
                            self.fields[k][j]['bg'] = 'SystemButtonFace'
                    for k in range(6, 13):
                        if self.players[self.player].used[k] == False:
                            self.fields[k+2][j]['state'] = 'normal'
                            self.fields[k+2][j]['bg'] = 'SystemButtonFace'
        # 다시 Roll Dice 과 diceButtons 버튼 활성화 , bottomLabel 초기화
        self.rollDice['state'] = 'normal'
        self.rollDice['bg'] = 'SystemButtonFace'
        self.rollDice['text'] = 'Roll Dice'
        self.roll = 0
        self.bottomLabel.config(text=self.players[self.player].toString() + "차례: Roll Dice 버튼을 누르세요")
        for i in range(5):    # dice 버튼 5 개 생성
            self.diceButtons[i]['state'] = 'normal'
            self.diceButtons[i]['bg'] = 'SystemButtonFace'
            self.diceButtons[i]['text'] = '?'
        # 라운드 증가 시키고 종료 검사
        if (self.player == 0):
            self.round += 1
        if (self.round == 13):
            game_result = []
            for i in range(len(self.players)):
                game_result.append(self.players[i].getTotalScore())
            for i in self.players:
                if i.getTotalScore() == max(game_result):
                    self.bottomLabel.config(text=i.toString() + "의 승리 ! ! !")


YahtzeeBoard()