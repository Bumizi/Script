from tkinter import*
import random
class TicTacToe:
    def again(self):
        for r in range(3):
            for c in range(3):
                self.labelList[r * 3 + c].configure(image=self.imageList[random.randint(0, 1)])

    def check(self, r, c, ox):
        if c == 0:
            if self.Matrix[r][c+1] == self.Matrix[r][c+2] == ox:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                else:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                return
            elif self.Matrix[r+1][c+1] == self.Matrix[r+2][c+2] == ox:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                else:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                return
        elif c == 1:
            if self.Matrix[r][c-1] == self.Matrix[r][c+1] == ox:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                else:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                return
        elif c == 2:
            if self.Matrix[r][c - 1] == self.Matrix[r][c - 2] == ox:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                else:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                return
        if r == 0:
            if self.Matrix[r+1][c] == self.Matrix[r+2][c] == ox:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                else:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                return
        elif r == 1:
            if self.Matrix[r - 1][c] == self.Matrix[r + 1][c] == ox:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                else:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                return
        elif r == 2:
            if self.Matrix[r - 1][c] == self.Matrix[r - 2][c] == ox:
                if ox == 0:
                    self.explain = Label(self.frame2, text="O 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                else:
                    self.explain = Label(self.frame2, text="X 승리! 게임이 끝났습니다.")
                    self.explain.pack()
                return

    def pressed(self, r, c):
        if self.Matrix[r][c] == 2:
            if self.turn: #O의 차례
                self.buttonList[r * 3 + c].configure(image=self.imageList[0])
                self.Matrix[r][c] = 0
                self.check(r, c, 0)
            else:
                self.buttonList[r * 3 + c].configure(image=self.imageList[1])
                self.Matrix[r][c] = 1
                self.check(r, c, 1)
            self.turn = not self.turn

    def __init__(self):
        window = Tk()
        # again에서 다시 바꿔야하기 때문에 변수들을 instance 변수, 즉 멤버변수로 만들어줘야 접근할 수 있다.
        self.imageList = []
        self.imageList.append(PhotoImage(file='image/o.gif'))
        self.imageList.append(PhotoImage(file='image/x.gif'))
        self.imageList.append(PhotoImage(file='image/empty.gif'))
        self.labelList = []

        self.buttonList = []
        self.Matrix = [[0] * 3 for i in range(3)]
        self.turn = True #Ture = O 의 차례, False = X의 차례
        frame1 = Frame(window)
        frame1.pack()
        for r in range(3):
            for c in range(3):
                self.buttonList.append(Button(frame1, image=self.imageList[2], command=lambda Row=r, Col=c : self.pressed(Row, Col)))
                self.Matrix[r][c] = 2
                #self.labelList.append(Label(frame1, image=self.imageList[random.randint(0, 1)]))
                self.buttonList[r*3+c].grid(row=r, column=c)
                #self.labelList[r*3+c].grid(row=r, column=c)
        self.frame2 = Frame(window)
        self.frame2.pack()
        #self.explain = Label(self.frame2, text="O 차례")
        #self.explain.pack()

        window.mainloop()

TicTacToe()