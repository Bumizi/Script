from tkinter import *
import tkinter.messagebox
import random

class Linear:
    def __init__(self):
        window = Tk()

        self.index = 0
        self.width = 700
        self.height = 400
        self.barW = (self.width - 20) / 20
        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Label(frame, text="키를 입력: ").pack(side=LEFT)
        self.e = Entry(frame, text='', justify=RIGHT, width=3) # 여기에 pack()하면 안 됨.
        self.e.pack(side=LEFT)

        Button(frame, text="다음단계", command=self.step).pack(side=LEFT)
        Button(frame, text="재설정", command=self.reset).pack(side=LEFT)

        window.mainloop()

    def step(self):
        minIndex = self.index
        for i in range(self.index + 1, 20):  # i=self.i, ... 20 중에서 minimum 찾는다.
            if self.numbers[minIndex] > self.numbers[i]:
                minIndex = i
        self.numbers[self.index], self.numbers[minIndex] = self.numbers[minIndex], self.numbers[self.index]
        self.canvas.delete("graph")
        self.draw()

        self.canvas.delete("red")
        self.canvas.create_rectangle(10 + self.index * self.barW, ((self.height - 20) * (1 - self.numbers[self.index] / 20)) + 17,
                                     10 + (self.index + 1) * self.barW, self.height - 10, fill='red', tags="red")

        self.index += 1

    def reset(self):
        self.numbers = [x for x in range(1, 21)]  # 1~20까지의 숫자를 필터링하는데 아무것도 안하고 넣음.
        random.shuffle(self.numbers)
        self.canvas.delete("red")
        self.index = 0
        self.draw()

    def draw(self):
        self.canvas.delete("graph")
        for i in range(20):
            self.canvas.create_rectangle(10 + i*self.barW, (17 + (self.height-20)*(1 - self.numbers[i]/20)),
                                         10 + (i+1)*self.barW, self.height - 10, tags="graph")
            self.canvas.create_text(20 + i*self.barW, (7 + (self.height - 20) * (1-self.numbers[i]/20)), text=str(self.numbers[i]), tags="graph")

def selectionSort(x):
    length = len(x)
    for i in range(length-1):
        indexMin = i
        for j in range(i+1, length):
            if x[indexMin] > x[j]:
                indexMin = j
        x[i], x[indexMin] = x[indexMin], x[i]
    return x

Linear()

