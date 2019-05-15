from tkinter import *
import tkinter.messagebox
import random

g_Tk = Tk()
g_Tk.geometry("800x600+750+200")
g_Tk.title("공연 / 전시 정보 조회 서비스")
frame = Frame(g_Tk)
frame.pack(fill=BOTH, ipadx=0, ipady=50, padx=0, pady=0, side=TOP)
DataList = []
SearchMode = 0

def InitTopText():
    MainText = Label(g_Tk, text="[공연 / 전시 정보검색 서비스]")
    MainText.pack()
    MainText.place(x=330)

def SearchCategoryButton():

    AreaSearch = Button(frame, text="지역별", command=InitSearchByArea)
    AreaSearch.pack()
    AreaSearch.place(x=10, y=10)
    PeriodSearch = Button(frame, text="기간별", command=InitSearchByPeriod)
    PeriodSearch.pack()
    PeriodSearch.place(x=70, y=10)
    RealmSearch = Button(frame, text="분야별", command=SearchButtonAction)
    RealmSearch.pack()
    RealmSearch.place(x=130, y=10)

def InitSearchByArea():

    area = Label(g_Tk, text="지역별 검색")
    area.pack()
    area.place(x=130, y=50)

    sido = Label(g_Tk, text="시 / 도")
    sido.pack()
    sido.place(x=30, y=100)

    gugun = Label(g_Tk, text="구 / 군")
    gugun.pack()
    gugun.place(x=30, y=150)

    global sidoInputLabel
    sidoInputLabel = Entry(g_Tk, width=26, borderwidth=6, relief='ridge')
    sidoInputLabel.pack()
    sidoInputLabel.place(x=80, y=95)

    global gugunInputLabel
    gugunInputLabel = Entry(g_Tk, width=26, borderwidth=6, relief='ridge')
    gugunInputLabel.pack()
    gugunInputLabel.place(x=80, y=145)

    #sidoScrollbar = Scrollbar(g_Tk)
    #sidoScrollbar.pack(fill="y")
    #sidoScrollbar.place(x=240, y=85)
    #sidoListBox = Listbox(g_Tk, activestyle='none', width=15, height=1, borderwidth=12, relief='ridge', yscrollcommand=sidoScrollbar.set)
    #sidoListBox.pack()
    #sidoListBox.place(x=100, y=90)
    #sidoScrollbar.config(command=sidoListBox.yview)

def InitSearchByPeriod():

    period = Label(g_Tk, text="기간별 검색")
    period.pack()
    period.place(x=130, y=50)

    start = Label(g_Tk, text="시작")
    start.pack()
    start.place(x=10, y=100)

    end = Label(g_Tk, text="종료")
    end.pack()
    end.place(x=10, y=150)

    sido = Label(g_Tk, text="시 / 도")
    sido.pack()
    sido.place(x=30, y=100)

    gugun = Label(g_Tk, text="구 / 군")
    gugun.pack()
    gugun.place(x=30, y=150)

    global sidoInputLabel
    sidoInputLabel = Entry(g_Tk, width=26, borderwidth=6, relief='ridge')
    sidoInputLabel.pack()
    sidoInputLabel.place(x=80, y=95)

    global gugunInputLabel
    gugunInputLabel = Entry(g_Tk, width=26, borderwidth=6, relief='ridge')
    gugunInputLabel.pack()
    gugunInputLabel.place(x=80, y=145)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=1500, y=50)
    SearchListBox = Listbox(g_Tk, activestyle='none', width=10, height=1, borderwidth=12, relief='ridge', yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화시설")
    SearchListBox.pack()
    SearchListBox.place(x=500, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    InputLabel = Entry(g_Tk, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=1000, y=105)

def InitSearchButton():
    SearchButton = Button(g_Tk, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=320, y=125)

def SearchButtonAction():
    global SearchListBox, SearchMode
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    if SearchMode == 0: #지역별 검색
        pass
    elif SearchMode == 1: #기간별 검색
        pass
    elif SearchMode == 2: #분야별 검색
        pass

    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()
    RenderText.configure(state='disabled')

def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()
    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes
            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
                    if subitems[3].firstChild.nodeValue == InputLabel.get():  #
                        pass
                    elif subitems[5].firstChild.nodeValue == InputLabel.get():  #
                        pass
                    else:
                        continue
                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass  #
                        if tel[0] is not '0':
                            tel = "02-" + tel
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))
                for i in range(len(DataList)):
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, i + 1)
                    RenderText.insert(INSERT, "] ")
                    RenderText.insert(INSERT, "시설명: ")
                    RenderText.insert(INSERT, DataList[i][0])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "주소: ")
                    RenderText.insert(INSERT, DataList[i][1])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "전화번호: ")
                    RenderText.insert(INSERT, DataList[i][2])
                    RenderText.insert(INSERT, "\n\n")


def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

SearchCategoryButton()
#InitSearchByArea()
#InitSearchByPeriod()

InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
g_Tk.mainloop()

