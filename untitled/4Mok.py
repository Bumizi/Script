from tkinter import*
import random
class play4Mok:
    def again(self):
        for r in range(6):
            for c in range(7):
                self.buttonList[r * 7 + c].configure(image=self.imageList[2])
                self.buttonList[r * 7 + c].configure(text=' ')
                self.Matrix[r][c] = 2
        self.win = False
        self.explain.destroy()

    def pressed(self, r, c):
        if not self.win:
            for i in range(5, -1, -1): # i = 5, 4, 3, 2, 1, 0
                if self.buttonList[i*7+c]['text'] == ' ': #비어있는 셀이냐?
                    if self.turn:  # O의 차례
                        self.buttonList[i * 7 + c].configure(image=self.imageList[0])
                        self.buttonList[i * 7 + c].configure(text='O')
                        self.Matrix[i][c] = 0
                        self.check(i, c, 0)
                    else:
                        self.buttonList[i * 7 + c].configure(image=self.imageList[1])
                        self.buttonList[i * 7 + c].configure(text='X')
                        self.Matrix[i][c] = 1
                        self.check(i, c, 1)
                    self.turn = not self.turn
                    break

    def check(self, r, c, ox):
        if r <= 2 and ox == self.Matrix[r+1][c] == self.Matrix[r+2][c] == self.Matrix[r+3][c]:
            if ox == 0:
                self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
            elif ox == 1:
                self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
            self.explain.pack()
            self.win = True
            return
        elif r <= 2 and c >= 3:
            if ox == self.Matrix[r+1][c-1] == self.Matrix[r+2][c-2] == self.Matrix[r+3][c-3]:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                elif ox == 1:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                self.explain.pack()
                self.win = True
                return
        elif r <= 2 and c <= 3:
            if ox == self.Matrix[r + 1][c + 1] == self.Matrix[r + 2][c + 2] == self.Matrix[r + 3][c + 3]:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                elif ox == 1:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                self.explain.pack()
                self.win = True
                return
        else:
            cnt = 0
            i = 0
            while( c-i >= 0 and c-i < 7 and  self.Matrix[r][c-i] == ox ):
                i += 1
                cnt += 1
            i = 1
            while( c+i >= 0 and c+i < 7 and self.Matrix[r][c+i] == ox ):
                i += 1
                cnt += 1
            if cnt == 4:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                elif ox == 1:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                self.explain.pack()
                self.win = True
                return

    def __init__(self):
        window = Tk()
        # again에서 다시 바꿔야하기 때문에 변수들을 instance 변수, 즉 멤버변수로 만들어줘야 접근할 수 있다.
        self.imageList = []
        self.imageList.append(PhotoImage(file='image/o.gif'))
        self.imageList.append(PhotoImage(file='image/x.gif'))
        self.imageList.append(PhotoImage(file='image/empty.gif'))
        #self.labelList = []
        self.buttonList = []
        self.turn = True #Ture = O 의 차례, False = X의 차례
        self.win = False
        frame1 = Frame(window)
        frame1.pack()
        self.Matrix = [[0] * 7 for i in range(6)]
        for r in range(6):
            for c in range(7):
                self.buttonList.append(Button(frame1, text=' ', image=self.imageList[2], command=lambda Row=r, Col=c : self.pressed(Row, Col)))
                self.buttonList[r*7+c].grid(row=r, column=c)
                self.Matrix[r][c] = 2
        self.frame2 = Frame(window)
        self.frame2.pack()
        self.explain = Button(self.frame2, text="새로시작", command=self.again)
        self.explain.pack()

        window.mainloop()

play4Mok()